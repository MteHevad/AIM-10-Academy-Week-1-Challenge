import pandas as pd
import matplotlib.pyplot as plt

# Load news dataset
news_data = pd.read_csv('C:/raw_analyst_ratings.csv')

# Convert news date to datetime
news_data['date'] = pd.to_datetime(news_data['date'], errors='coerce')

# Aggregate the number of articles published per day
daily_article_counts = news_data.groupby('date').size().reset_index(name='article_count')

# Plotting daily fluctuations in the number of articles published
plt.figure(figsize=(12, 6))
plt.plot(daily_article_counts['date'], daily_article_counts['article_count'], marker='o', linestyle='-', color='b', label='Number of Articles')

# Overlay key market events (example: key market events dates)
# You may define actual events by adding these as needed
key_market_events = {
    '2024-01-15': 'Earnings Report',
    '2024-03-10': 'New Product Launch',
    '2024-05-20': 'Major Acquisition Announcement'
}

for event_date, event_name in key_market_events.items():
    plt.axvline(pd.to_datetime(event_date), color='r', linestyle='--', linewidth=1)
    plt.text(pd.to_datetime(event_date), max(daily_article_counts['article_count']), event_name, rotation=90, verticalalignment='bottom', color='r')

# Customizing the plot
plt.title('Daily Fluctuations in the Number of Articles Published')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.legend()
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
