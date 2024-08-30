import pandas as pd
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt

# Ensure nltk dependencies are downloaded
nltk.download('stopwords')

# Set the file path
file_path = r"C:\raw_analyst_ratings.csv"

# Load the dataset
try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except PermissionError as e:
    print(f"Permission error: {e}")
    exit()
except FileNotFoundError as e:
    print(f"File not found: {e}")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# Topic Modeling: Common Words
def get_common_words(texts, num_words=20):
    stop_words = set(stopwords.words('english'))
    all_words = ' '.join(texts).lower().split()
    filtered_words = [word for word in all_words if word.isalpha() and word not in stop_words]
    word_freq = Counter(filtered_words)
    return word_freq.most_common(num_words)

common_words = get_common_words(df['headline'])
print("\nMost Common Words:")
print(common_words)

# Create and display a word cloud
text = ' '.join(df['headline'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Headlines')
plt.show()
