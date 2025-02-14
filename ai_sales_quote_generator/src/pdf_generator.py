# src/pdf_generator.py
from fpdf import FPDF
import os
from config import OUTPUT_DIR

def save_quote_as_pdf(quote):
    """Generate and save a PDF from the quote details."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, f"Quote for {quote['company_name']}", ln=True, align='C')
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, f"Reference: {quote['reference_number']}", ln=True, align='C')

    pdf.cell(200, 10, "-"*60, ln=True)

    # Quote Info
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, f"Created Date: {quote['created_date']}", ln=True)
    pdf.cell(200, 10, f"Expires Date: {quote['expires_date']}", ln=True)
    pdf.cell(200, 10, f"Company Address: {quote['address']}", ln=True)

    pdf.cell(200, 10, "-"*60, ln=True)

    # Products Section
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Products & Services:", ln=True)
    pdf.set_font("Arial", size=10)

    for product in quote['products']:
        product_line = f"{product['name']} - Qty: {product['quantity']} @ ${product['price']} each"
        pdf.cell(200, 10, product_line, ln=True)

    pdf.cell(200, 10, "-"*60, ln=True)

    # Purchase Terms
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Purchase Terms:", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 10, quote['purchase_terms'] if quote['purchase_terms'] else "No special terms")

    # Save PDF
    output_path = os.path.join(OUTPUT_DIR, f"Quote_{quote['reference_number']}.pdf")
    pdf.output(output_path)
    print(f"✅ Quote saved as PDF: {output_path}")