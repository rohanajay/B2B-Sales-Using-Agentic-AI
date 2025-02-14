# src/test_generate_quote.py
from generate_quote import generate_quote

# Sample product list
products = [
    {"name": "Enterprise Support", "quantity": 3, "price": 1500},
    {"name": "Managed Cloud Platform", "quantity": 1, "price": 12000}
]

# Generate quote
quote = generate_quote(
    company_name="TechNova Inc.",
    address="123 Innovation Drive, Silicon Valley, CA",
    products=products,
    purchase_terms="50% payment upfront, remainder upon delivery."
)

# Display the generated quote
print("Generated Quote:")
for key, value in quote.items():
    print(f"{key}: {value}")