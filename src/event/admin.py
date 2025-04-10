from django.contrib import admin  
from django.http import HttpResponse
from .models import Events

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

@admin.register(Events)
class ServiceEvents(admin.ModelAdmin):
    list_per_page = 10
    list_display = (
        "title",
        "date",
        "description"
    )
    actions = ['download_pdf']

    def download_pdf(self, request, queryset):
        model_name = self.model.__name__
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={model_name}.pdf'

        # Use A4 in landscape mode
        pdf = canvas.Canvas(response, pagesize=landscape(A4))
        pdf.setTitle(f'{model_name} PDF Report')

        width, height = landscape(A4)  # Get width/height in landscape

        # Title and Subtitle
        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawCentredString(width / 2, height - 50, "Diksha's Fitness Studio")

        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawCentredString(width / 2, height - 80, "Event Details")

        # Exclude image field from table
        fields_to_include = [field for field in self.model._meta.fields if field.name != 'image']

        headers = [field.verbose_name.title() for field in fields_to_include]
        data = [headers]

        for obj in queryset:
            row = [str(getattr(obj, field.name)) for field in fields_to_include]
            data.append(row)

        # Adjust column widths for landscape
        column_widths = [35, 75, 150, 175, 300, 100]  # Customize widths as needed

        table = Table(data, colWidths=column_widths, repeatRows=1)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('FONT', (0, 0), (-1, -1), 'Helvetica', 9),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ]))

        # Adjust table position
        table_x = 2
        table_y = height - 120 - (20 * len(data))

        table.wrapOn(pdf, width, height)
        table.drawOn(pdf, table_x, max(table_y, 50))  # Prevent drawing off the page

        pdf.save()
        return response

    download_pdf.short_description = "Download selected events as PDF"
