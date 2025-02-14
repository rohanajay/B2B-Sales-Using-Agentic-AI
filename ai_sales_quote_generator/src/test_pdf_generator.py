# src/test_pdf_generator.py
from generate_quote import generate_quote
from pdf_generator import save_quote_as_pdf

# Sample product list
products = [
    {"name": "Enterprise Support", "quantity": 2, "price": 1500},
    {"name": "AI Integration Service", "quantity": 1, "price": 5000}
]

# Generate a sample quote
quote = generate_quote(
    company_name="NextGen Solutions",
    address="456 Future Way, Tech City, CA",
    products=products,
    purchase_terms="Payment due within 15 days of receipt of invoice."
)

# Generate and save the quote as a PDF
save_quote_as_pdf(quote)