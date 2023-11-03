import pandas as pd 
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from matplotlib import pyplot as plt 
from collections import Counter

data = [
    [
[('like', 54), ('great', 44), ('team', 43), ('love', 40), ('player', 37), ('best', 35), ('i', 34), ('game', 30), ('jordan', 23), ('play', 22)], 
[('team', 13), ('never', 11), ('year', 10), ('kobe', 8), ('the', 7), ('would', 7), ('he', 7), ('lebron', 7), ('get', 6), ('player', 6)] ,
[('team', 16), ('i', 12), ('leah', 11), ('time', 10), ('lucy', 8), ('see', 8), ('the', 8), ('england', 8), ('game', 7), ('im', 7)] ,], 

[[('great', 28), ('jordan', 23), ('like', 23), ('player', 23), ('team', 21), ('game', 17), ('lebron', 16), ('best', 16), ('good', 13), ('win', 12)] ,
[('team', 10), ('never', 10), ('year', 9), ('kobe', 8), ('he', 7), ('lebron', 7), ('final', 6), ('hell', 6), ('jordan', 6), ('nba', 6)] ,
[('team', 8), ('lebron', 7), ('kd', 6), ('time', 6), ('jordan', 6), ('nba', 6), ('college', 5), ('player', 5), ('never', 5), ('mvp', 4)] ,],

[[('love', 18), ('like', 11), ('lucy', 9), ('leah', 8), ('i', 7), ('best', 7), ('game', 7), ('it', 7), ('sunny', 7), ('look', 6)] ,
[('lucy', 2), ('bit', 2), ('the', 2), ('useless', 2), ('absolutely', 2), ('no', 2), ('wever', 2), ('way', 2), ('sad', 2), ('stopped', 2)] ,
[('i', 7), ('lucy', 7), ('leah', 7), ('jack', 5), ('now', 4), ('irish', 4), ('room', 4), ('know', 4), ('pound', 4), ('who', 4)] ,],


[[('2', 7), ('team', 7), ('great', 6), ('player', 6), ('ayoka', 5), ('play', 5), ('better', 4), ('let', 4), ('go', 4), ('get', 3)], 
[('shoot', 2), ('would', 2), ('threat', 2), ('team', 2), ('dominant', 1), ('paint', 1), ('three', 1), ('pull', 1), ('rebound', 1), ('several', 1)] ,
[('english', 3), ('the', 3), ('woman', 3), ('speaks', 2), ('han', 2), ('coach', 2), ('translator', 2), ('ayoka', 2), ('lee', 2), ('clark', 2)] ,],

[[('love', 34), ('like', 29), ('i', 25), ('best', 18), ('team', 15), ('it', 13), ('need', 12), ('england', 12), ('leah', 12), ('lucy', 11)] ,
[('lucy', 3), ('the', 3), ('sad', 3), ('food', 3), ('absolutely', 2), ('understand', 2), ('way', 2), ('stopped', 2), ('growing', 2), ('one', 2)] ,
[('leah', 11), ('i', 10), ('lucy', 8), ('england', 8), ('team', 8), ('see', 7), ('jack', 6), ('rice', 6), ('world', 5), ('v', 5)] 
]]

pos_words = [
   [('team', 16), ('i', 12), ('leah', 11), ('time', 10), ('lucy', 8), ('see', 8), ('the', 8), ('england', 8), ('game', 7), ('im', 7)] ,
   [('team', 8), ('lebron', 7), ('kd', 6), ('time', 6), ('jordan', 6), ('nba', 6), ('college', 5), ('player', 5), ('never', 5), ('mvp', 4)],
    [('i', 7), ('lucy', 7), ('leah', 7), ('jack', 5), ('now', 4), ('irish', 4), ('room', 4), ('know', 4), ('pound', 4), ('who', 4)],
   [('english', 3), ('the', 3), ('woman', 3), ('speaks', 2), ('han', 2), ('coach', 2), ('translator', 2), ('ayoka', 2), ('lee', 2), ('clark', 2)],
   [('leah', 11), ('i', 10), ('lucy', 8), ('england', 8), ('team', 8), ('see', 7), ('jack', 6), ('rice', 6), ('world', 5), ('v', 5)] 
]

import numpy as np
# Sentiments
sentiments = ['Neutral']

# Number of top words to display
num_top_words = 10

# Select the top N words for the positive sentiment
top_words = [words[:num_top_words] for words in pos_words]
word_counts = [counts[:num_top_words] for counts in pos_words]

# Create a stacked bar chart for positive words across datasets
x = np.arange(num_top_words)  # X-axis values
width = 0.25  # Width of the bars

fig, ax = plt.subplots(figsize=(12, 6))

for i, sentiment in enumerate(sentiments):
    bottom = np.zeros(num_top_words, dtype=int)  # Initialize with zeros of integer data type
    for j in range(len(pos_words)):
        counts = [int(count[1]) for count in word_counts[j]]  # Extract the counts
        ax.bar(x + i * width, counts, width, label=f'{sentiment} - Dataset {j + 1}', bottom=bottom)
        bottom += np.array(counts)

ax.set_xlabel('Top Words')
ax.set_ylabel('Counts')
ax.set_title('Stacked Bar Chart of Top Positive Words Across Datasets')
ax.set_xticks(x + (width * (len(sentiments) - 1) / 2))
ax.set_xticklabels([word[0] for word in top_words[0]], rotation=45, ha="right")
ax.legend()

plt.tight_layout()
plt.show()





