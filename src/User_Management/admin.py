from django.contrib import admin
from django.http import HttpResponse
from .models import User_Management
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

@admin.register(User_Management)
class UserManagementAdmin(admin.ModelAdmin):
    list_display = (
        'Client_Name',
        "Subscription_Type",
        "Subscription_Date_From",
        "Subscription_Date_To",
        "Mobile_No",
        "Address",
        "Batch_Time",
        "Blood_Group",
        "Weight",
        "Height",
        "Medical_Issue",
        "Taking_Medicine",
        "Reason_For_Joining",
    )
    list_per_page = 10
    actions = ['download_pdf']

    def download_pdf(self, request, queryset):
        model_name = self.model.__name__
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={model_name}_report.pdf'

        # Create PDF in landscape mode
        pdf = canvas.Canvas(response, pagesize=landscape(A4))
        pdf.setTitle(f'{model_name} Report')

        page_width, page_height = landscape(A4)

        # Add headers
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawCentredString(page_width / 2, page_height - 50, "Diksha's Fitness Studio")
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawCentredString(page_width / 2, page_height - 80, "Client Details Report")

        if not queryset:
            pdf.setFont("Helvetica", 12)
            pdf.drawString(100, page_height - 120, "No client records selected to export.")
            pdf.save()
            return response

        # Prepare data
        fields = [field for field in self.model._meta.fields]
        headers = [field.verbose_name for field in fields]
        data = [headers]

        for obj in queryset:
            row = [str(getattr(obj, field.name)) if getattr(obj, field.name) is not None else "" for field in fields]
            data.append(row)

        # Adjust column widths (evenly distribute across the page width)
        num_cols = len(headers)
        margin = inch
        usable_width = page_width - 2 * margin
        col_width = usable_width / num_cols
        col_widths = [col_width] * num_cols

        # Create and style the table
        table = Table(data, colWidths=col_widths, repeatRows=1)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f0f0f0')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('TOPPADDING', (0, 0), (-1, 0), 3),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ]))

        # Position table in the middle horizontally
        table_width, table_height = table.wrap(0, 0)
        x_position = (page_width - table_width) / 2
        y_position = page_height - table_height - 120  # Leave space below heading

        # Draw the table
        table.wrapOn(pdf, page_width, page_height)
        table.drawOn(pdf, x_position, y_position)

        pdf.save()
        return response

