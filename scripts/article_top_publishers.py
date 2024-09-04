import pandas as pd
import matplotlib.pyplot as plt

# Load the news dataset
file_path = 'C:/raw_analyst_ratings.csv'
news_data = pd.read_csv(file_path)

# Convert the date column to datetime
news_data['date'] = pd.to_datetime(news_data['date'], errors='coerce')

# Extract year and month from the date for monthly grouping
news_data['year_month'] = news_data['date'].dt.to_period('M')

# Group by month and count the number of articles
articles_per_month = news_data.groupby('year_month').size().reset_index(name='article_count')

# Plotting the line graph
plt.figure(figsize=(12, 6))
plt.plot(articles_per_month['year_month'].astype(str), articles_per_month['article_count'], marker='o', linestyle='-', color='b', label='Number of Articles')

# Mark significant peaks with major financial events
significant_peaks = articles_per_month.sort_values(by='article_count', ascending=False).head(3)  # Modify this as per your event dates
for idx, row in significant_peaks.iterrows():
    plt.annotate(f"Peak: {row['year_month']}", 
                 xy=(row['year_month'].strftime('%Y-%m'), row['article_count']), 
                 xytext=(10, 20), 
                 textcoords='offset points', 
                 arrowprops=dict(arrowstyle='->', color='red'))

plt.title('Number of Articles Published per Month with Significant Peaks')
plt.xlabel('Month')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
