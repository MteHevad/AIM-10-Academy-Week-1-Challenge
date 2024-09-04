import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Ensure nltk dependencies are downloaded
nltk.download('vader_lexicon')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Load news dataset
news_data = pd.read_csv('C:/raw_analyst_ratings.csv')

# Convert news date to datetime and extract the date part
news_data['date'] = pd.to_datetime(news_data['date'], errors='coerce')
news_data['date'] = news_data['date'].dt.date

# Perform sentiment analysis on the news headlines
news_data['sentiment_score'] = news_data['headline'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Classify sentiment into categories (Positive, Neutral, Negative)
news_data['sentiment_label'] = news_data['sentiment_score'].apply(lambda x: 'Positive' if x > 0 else ('Neutral' if x == 0 else 'Negative'))

# Calculate sentiment distribution
sentiment_distribution = news_data['sentiment_label'].value_counts()

# Plot pie chart for sentiment distribution
plt.figure(figsize=(8, 6))
plt.pie(sentiment_distribution, labels=sentiment_distribution.index, autopct='%1.1f%%', colors=['#66b3ff', '#99ff99', '#ffcc99'])
plt.title('Distribution of Sentiments Among Headlines')
plt.savefig('C:/sentiment_distribution_pie_chart.png')
plt.show()

# Plot bar graph for sentiment distribution
plt.figure(figsize=(8, 6))
sentiment_distribution.plot(kind='bar', color=['#66b3ff', '#99ff99', '#ffcc99'])
plt.title('Distribution of Sentiments Among Headlines')
plt.xlabel('Sentiment')
plt.ylabel('Number of Headlines')
plt.savefig('C:/sentiment_distribution_bar_chart.png')
plt.show()
