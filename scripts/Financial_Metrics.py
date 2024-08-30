from pynance import Financials

# Function to calculate financial metrics for each company's data
def calculate_financial_metrics(df):
    financials = Financials(df)
    
    # Example: Calculate annual returns
    annual_returns = financials.annual_returns()
    print("Annual Returns:")
    print(annual_returns)

# Calculate metrics for each company's data
for company, df in company_data.items():
    print(f"\nCalculating financial metrics for {company}:")
    calculate_financial_metrics(df)
