from django.contrib import admin
from django.http import HttpResponse
from .models import ClassInfo
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate

from reportlab.lib.styles import ParagraphStyle

@admin.register(ClassInfo)
class ClassInfoAdmin(admin.ModelAdmin):
    list_display = (
        'class_title',
        'class_week',
        'class_time',
        'class_description',
        'class_img',
    )
    list_per_page = 10
    actions = ['download_pdf']

    def download_pdf(self, request, queryset):
        model_name = self.model.__name__
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={model_name}_report.pdf'

        pdf = canvas.Canvas(response, pagesize=landscape(A4))
        pdf.setTitle(f'{model_name} Report')

        page_width, page_height = landscape(A4)

        # Header
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawCentredString(page_width / 2, page_height - 50, "Diksha's Fitness Studio")
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawCentredString(page_width / 2, page_height - 80, "Class Information Report")

        if not queryset:
            pdf.setFont("Helvetica", 12)
            pdf.drawString(100, page_height - 120, "No class records selected to export.")
            pdf.save()
            return response

        # Data Preparation
        fields = [field for field in self.model._meta.fields]
        headers = [field.verbose_name for field in fields]
        data = [headers]

        # Use paragraph for long text fields
        styles = getSampleStyleSheet()
        wrap_style = ParagraphStyle(name='WrapStyle', fontSize=8, leading=10, alignment=TA_LEFT)

        for obj in queryset:
            row = []
            for field in fields:
                value = getattr(obj, field.name)
                text = str(value) if value else ""
                # Wrap long text using Paragraph
                row.append(Paragraph(text, wrap_style))
            data.append(row)

        # Calculate dynamic column widths with a max cap
        num_cols = len(headers)
        margin = inch
        usable_width = page_width - 2 * margin

        # Approximate max width based on content length
        max_lens = [max(len(str(getattr(obj, f.name))) for obj in queryset) if queryset else 10 for f in fields]
        total_len = sum(max_lens)
        col_widths = [min((l / total_len) * usable_width, 200) for l in max_lens]

        # Create table
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

        # Draw table in center
        table_width, table_height = table.wrap(0, 0)
        x_position = (page_width - table_width) / 2
        y_position = page_height - table_height - 120

        table.wrapOn(pdf, page_width, page_height)
        table.drawOn(pdf, x_position, y_position)

        pdf.save()
        return response

    download_pdf.short_description = "Download PDF report for selected classes"
