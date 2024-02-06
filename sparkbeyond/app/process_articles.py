from collections import Counter
import os
import re

def process_articles(folder_path, num_articles=4, top_n=10):
    articles = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            with open(os.path.join(folder_path, filename), 'r') as file:
                articles.append(file.read())

    words = re.findall(r'\b\w+\b', ' '.join(articles).lower())
    word_counts = Counter(words)

    return word_counts.most_common(top_n)
