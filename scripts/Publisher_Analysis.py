# Extract unique domains from publisher email addresses
df['publisher_domain'] = df['publisher'].apply(lambda x: x.split('@')[-1] if '@' in x else x)
domain_counts = df['publisher_domain'].value_counts()
print("Unique Domains and Their Counts:\n", domain_counts)

# Plot the top 10 domains
plt.figure(figsize=(10, 6))
domain_counts.head(10).plot(kind='bar', color='coral')
plt.title('Top 10 Most Active Publisher Domains')
plt.xlabel('Domain')
plt.ylabel('Number of Articles')
plt.xticks(rotation=45)
plt.show()
