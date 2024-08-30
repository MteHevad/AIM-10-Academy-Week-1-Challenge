# Extract the hour of publication
df['hour'] = df['date'].dt.hour

# Plot the number of articles published by hour
plt.figure(figsize=(10, 5))
df['hour'].value_counts().sort_index().plot(kind='bar', color='teal')
plt.title('Number of Articles Published by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)
plt.show()
