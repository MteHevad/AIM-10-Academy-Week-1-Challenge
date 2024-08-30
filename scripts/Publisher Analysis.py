import pandas as pd

# Set the file path
file_path = r"C:\raw_analyst_ratings.csv"

# Load the dataset
try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except PermissionError as e:
    print(f"Permission error: {e}")
    exit()
except FileNotFoundError as e:
    print(f"File not found: {e}")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Publisher Analysis
# Extract publisher domains
publisher_domains = df['publisher'].str.extract(r'@(\S+)')
print("\nUnique Publisher Domains:")
print(publisher_domains[0].value_counts())

# Additional insights
print("\nAdditional Insights:")
print(f"Total number of articles: {len(df)}")
print(f"Data span from {df['date'].min()} to {df['date'].max()}")
