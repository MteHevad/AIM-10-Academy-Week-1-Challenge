import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the news dataset
file_path = 'C:/raw_analyst_ratings.csv'
news_data = pd.read_csv(file_path)

# Convert the publication date to datetime format
news_data['date'] = pd.to_datetime(news_data['date'], errors='coerce')

# Remove any rows with missing dates
news_data = news_data.dropna(subset=['date'])

# Create a density plot for the publication date distribution
plt.figure(figsize=(12, 6))
sns.histplot(news_data['date'], bins=30, kde=True, color='blue', alpha=0.7)
plt.title('Distribution of Publication Dates with Key Events Annotated')
plt.xlabel('Publication Date')
plt.ylabel('Density')

# Annotate key events or peaks (manually defined or automatically detected)
# Example: Annotate peaks
peaks = news_data['date'].value_counts().idxmax()  # Finds the date with maximum publications
plt.axvline(peaks, color='red', linestyle='--')
plt.text(peaks, plt.ylim()[1] * 0.9, 'Peak', color='red', ha='right')

# Show plot
plt.tight_layout()
plt.show()
