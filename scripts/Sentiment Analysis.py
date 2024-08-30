# Sentiment analysis using TextBlob
df['sentiment_score'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['sentiment_label'] = df['sentiment_score'].apply(lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral'))

# Plot the sentiment distribution
plt.figure(figsize=(8, 5))
df['sentiment_label'].value_counts().plot(kind='bar', color='purple')
plt.title('Sentiment Distribution of Headlines')
plt.xlabel('Sentiment')
plt.ylabel('Number of Articles')
plt.show()

# Clean the headline text
df['headline_clean'] = df['headline'].str.lower().str.replace('[^\w\s]', '')

# Remove stopwords
stop_words = set(stopwords.words('english'))
df['keywords'] = df['headline_clean'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

# Generate a word cloud for the keywords
text = ' '.join(df['keywords'])
wordcloud = WordCloud(width=800, height=400, background_color='white', max_words=100).generate(text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Common Keywords in Headlines')
plt.show()
