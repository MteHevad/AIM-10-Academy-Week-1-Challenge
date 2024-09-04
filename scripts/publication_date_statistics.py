import pandas as pd
import matplotlib.pyplot as plt

# Load the news dataset
file_path = 'C:/raw_analyst_ratings.csv'
news_data = pd.read_csv(file_path)

# Ensure that the 'publisher' column exists
if 'publisher' not in news_data.columns:
    raise ValueError("The dataset must contain a 'publisher' column.")

# Count the number of articles per publisher
publisher_counts = news_data['publisher'].value_counts()

# Select the top contributors (top 10 in this case, adjust as needed)
top_publishers = publisher_counts.head(10)

# Plot a bar chart of the top contributors
plt.figure(figsize=(10, 6))
top_publishers.plot(kind='bar', color='skyblue')
plt.title('Number of Articles per Publisher (Top Contributors)')
plt.xlabel('Publisher')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the bar chart as an image
plt.savefig('C:/top_publishers_article_count.png')

# Display the bar chart
plt.show()
