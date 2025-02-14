import os
from fpdf import FPDF
from config import OUTPUT_DIR

def save_quote_as_pdf(quote):
    """Generate a PDF that matches the uploaded Word document layout without overlaps."""
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Enlarged Logo & Title Header
    logo_path = 'data/logo.png'
    if os.path.exists(logo_path):
        pdf.image(logo_path, x=10, y=10, w=35)  # Enlarged logo

    pdf.set_font('Arial', 'B', 22)
    pdf.cell(0, 20, 'Test company - Pilot', ln=True, align='C')
    pdf.ln(5)

    # Adjusted Two-Column Contact Information with Padding
    pdf.set_font('Arial', '', 10)
    left_col = f"""
{quote['company_name']}
{quote['address']}
Reference: {quote['reference_number']}
Quote created: {quote['created_date']}
"""
    right_col = """
Prediction Guard
101 N 4th St, Suite 234,
Lafayette, IN 47901
Prepared by: Sharan Shirodkar
Quote expires: {}
""".format(quote['expires_date'])

    pdf.multi_cell(95, 6, left_col, align='L')
    pdf.set_xy(105, pdf.get_y() - 30)
    pdf.multi_cell(95, 6, right_col, align='L')

    pdf.ln(10)

    # Enhanced Products & Services Table
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(70, 8, 'PRODUCTS & SERVICES', border=1, align='C')
    pdf.cell(30, 8, 'QUANTITY', border=1, align='C')
    pdf.cell(40, 8, 'PRICE', border=1, align='C', ln=True)

    pdf.set_font('Arial', '', 10)
    for product in quote['products']:
        pdf.cell(70, 8, product['name'], border=1, align='L')
        pdf.cell(30, 8, str(product['quantity']), border=1, align='C')
        pdf.cell(40, 8, f"${product['price']}/month", border=1, align='R', ln=True)

    # Summary Section with Proper Alignment
    total = sum(p['price'] * p['quantity'] for p in quote['products'])
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(90, 8, 'SUMMARY', border=1, align='L')
    pdf.cell(40, 8, f"${total:,.2f}", border=1, align='R', ln=True)

    pdf.ln(5)

    # Purchase Terms & Signature Area with Proper Spacing
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 8, 'Purchase Terms:', ln=True)
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 8, quote.get('purchase_terms', 'None provided'))
    pdf.ln(3)

    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 8, 'Signature:', ln=True)
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 8, '-'*50, ln=True)

    # Save PDF to output directory
    output_path = os.path.join(OUTPUT_DIR, f"Quote_{quote['reference_number']}.pdf")
    pdf.output(output_path)
    print(f"✅ Quote saved as PDF: {output_path}")