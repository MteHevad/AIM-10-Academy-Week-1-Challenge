import pandas as pd
import matplotlib.pyplot as plt

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

# Descriptive Statistics
print("Descriptive Statistics:")
df['headline_length'] = df['headline'].apply(len)
print("Headline Length Statistics:")
print(df['headline_length'].describe())

# Count articles per publisher
print("\nArticles per Publisher:")
print(df['publisher'].value_counts())

# Analyze publication dates
try:
    df['date'] = pd.to_datetime(df['date'], errors='coerce', infer_datetime_format=True)
    df['date'] = df['date'].dt.tz_localize(None)  # Remove timezone info if present
    print("\nPublication Dates Statistics:")
    print(df['date'].describe())
    
    # Plot articles per month
    df['year_month'] = df['date'].dt.to_period('M')
    df['year_month'].value_counts().sort_index().plot(kind='bar', title='Articles per Month')
    plt.xlabel('Month')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45)
    plt.show()
    
    # Plot articles by hour of the day
    df['hour'] = df['date'].dt.hour
    df.resample('D').size().plot(title='Number of Articles per Day')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles')
    plt.show()
    
    df['hour'].value_counts().sort_index().plot(kind='bar', title='Articles by Hour of Day')
    plt.xlabel('Hour')
    plt.ylabel('Number of Articles')
    plt.xticks(range(24), range(24))
    plt.show()
except Exception as e:
    print(f"An error occurred while processing dates: {e}")
