import pandas as pd 

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import nltk
nltk.download('punkt')  # Ensure you have the punkt tokenizer downloaded

def top_words(data): 
    full_words = []
    for word in o_odfs_words: 
        full_words.append(word.split())
    all_words = [word for doc in full_words for word in doc]

    # Count word frequencies
    word_counts = Counter(all_words)

    # Get the top 10 words
    top_words = word_counts.most_common(10)
    
    
    return top_words


o_pdf = pd.read_csv('wb_neutral_df.csv')
o_odfs_words = list(o_pdf['0'])[1:]
#print(full_words)

tw = top_words(o_odfs_words)
print(tw)

