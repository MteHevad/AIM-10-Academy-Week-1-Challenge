# Calculate the length of each headline
df['headline_length'] = df['headline'].str.len()

# Display basic statistics for headline lengths
headline_stats = df['headline_length'].describe()
print("Headline Length Statistics:\n", headline_stats)

# Plot the distribution of headline lengths
plt.figure(figsize=(8, 5))
sns.histplot(df['headline_length'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Headline Lengths')
plt.xlabel('Headline Length (characters)')
plt.ylabel('Frequency')
plt.show()

# Count articles per publisher
publisher_counts = df['publisher'].value_counts()
print("Number of Articles per Publisher:\n", publisher_counts)

# Plot the top 10 publishers
plt.figure(figsize=(10, 6))
publisher_counts.head(10).plot(kind='bar', color='green')
plt.title('Top 10 Most Active Publishers')
plt.xlabel('Publisher')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)
plt.show()

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], utc=True)
df['publication_date'] = df['date'].dt.date

# Plot the number of articles published over time
plt.figure(figsize=(12, 6))
df['publication_date'].value_counts().sort_index().plot()
plt.title('Article Publication Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.show()
