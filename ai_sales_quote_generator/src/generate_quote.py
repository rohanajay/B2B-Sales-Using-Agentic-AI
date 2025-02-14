# src/generate_quote.py
import random
import datetime

def generate_reference_number():
    """Generate a unique reference number based on timestamp and random number."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    random_num = random.randint(100000, 999999)
    return f"{timestamp}-{random_num}"

def generate_quote(company_name, address, products, purchase_terms=""):
    """Generate a quote dictionary with customizable fields."""
    return {
        "company_name": company_name,
        "address": address,
        "created_date": datetime.datetime.now().strftime("%B %d, %Y"),
        "expires_date": (datetime.datetime.now() + datetime.timedelta(days=90)).strftime("%B %d, %Y"),
        "reference_number": generate_reference_number(),
        "products": products,
        "purchase_terms": purchase_terms
    }