import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure nltk dependencies are downloaded
nltk.download('vader_lexicon')

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

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Perform sentiment analysis on headlines
df['sentiment'] = df['headline'].apply(lambda x: sia.polarity_scores(x)['compound'])
df['sentiment_label'] = df['sentiment'].apply(lambda x: 'Positive' if x > 0 else ('Neutral' if x == 0 else 'Negative'))

print("\nSentiment Analysis:")
print(df[['headline', 'sentiment_label']].head())
