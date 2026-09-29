import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_pdf_report(csv_file_path, output_pdf_path):
    # Load and handle missing data gracefully using pandas
    try:
        df = pd.read_csv(csv_file_path)
    except FileNotFoundError:
        print(f"Error: The file {csv_file_path} was not found.")
        return

    # Fill missing values to maintain clean tables
    df = df.fillna("N/A")

    # Calculate summary metrics
    total_records = len(df)
    summary_text_list = [f"Total Records Processed: {total_records}"]
    
    if 'Amount' in df.columns:
        total_amount = df['Amount'].sum() if pd.api.types.is_numeric_dtype(df['Amount']) else "N/A"
        summary_text_list.append(f"Total Amount: ${total_amount:,.2f}" if isinstance(total_amount, (int, float)) else f"Total Amount: {total_amount}")

    # Setup ReportLab Document
    doc = SimpleDocTemplate(output_pdf_path, pagesize=letter,
                            rightMargin=40, leftMargin=40,
                            topMargin=40, bottomMargin=40)
    story = []
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'ReportTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor("#1A237E"),
        spaceAfter=15
    )
    heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor("#3F51B5"),
        spaceBefore=10,
        spaceAfter=6
    )
    normal_style = styles['Normal']

    # Title
    story.append(Paragraph("Automated Business PDF Report", title_style))
    story.append(Spacer(1, 10))

    # Summary Section
    story.append(Paragraph("Summary Metrics", heading_style))
    for metric in summary_text_list:
        story.append(Paragraph(f"• {metric}", normal_style))
    story.append(Spacer(1, 15))

    # Data Table Section
    story.append(Paragraph("Data Overview", heading_style))
    
    # Convert dataframe to list for ReportLab Table
    table_data = [df.columns.tolist()] + df.values.tolist()

    # Create Table with formatting
    pdf_table = Table(table_data, repeatRows=1)
    pdf_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#3F51B5")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#F5F5F5")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.white),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFAFA")]),
    ]))

    story.append(pdf_table)

    # Build PDF
    doc.build(story)
    print(f"Report successfully generated: {output_pdf_path}")

if __name__ == "__main__":
    generate_pdf_report('sample_dataset.csv', 'output_report.pdf')
