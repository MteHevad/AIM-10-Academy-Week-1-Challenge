import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the news dataset
file_path = 'C:/raw_analyst_ratings.csv'
news_data = pd.read_csv(file_path)

# Convert news date to datetime to extract the hour
news_data['date'] = pd.to_datetime(news_data['date'], errors='coerce')

# Extract the hour from the datetime
news_data['hour'] = news_data['date'].dt.hour

# Group by hour to count the number of articles published each hour
hourly_article_count = news_data['hour'].value_counts().sort_index()

# Plotting the line graph for hourly article count
plt.figure(figsize=(12, 6))
plt.plot(hourly_article_count.index, hourly_article_count.values, marker='o', linestyle='-', color='b')
plt.title('Number of Articles Published by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Articles')
plt.xticks(range(0, 24))  # Set x-ticks from 0 to 23 for each hour
plt.grid(True)
plt.show()

# Plotting a heatmap for hourly article count (if needed)
plt.figure(figsize=(10, 6))
sns.heatmap(hourly_article_count.values.reshape(1, -1), annot=True, fmt="d", cmap="coolwarm", cbar=False, xticklabels=hourly_article_count.index)
plt.title('Heatmap of Articles Published by Hour')
plt.xlabel('Hour of the Day')
plt.yticks([])
plt.show()
