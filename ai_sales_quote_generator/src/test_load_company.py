from load_company import load_company_database, search_company

# Load the company database
df = load_company_database()

if df is not None:
    # Search for a company by user input
    company_name = input("Enter company name: ")
    company_info = search_company(company_name, df)

    if company_info:
        print("\nCompany Details Found:")
        for key, value in company_info.items():
            print(f"{key}: {value}")