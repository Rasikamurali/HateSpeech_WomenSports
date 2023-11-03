import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from matplotlib import pyplot as plt 
from collections import Counter

# Download VADER lexicon (do this only once)
nltk.download('vader_lexicon')

#all datasets 

overall = pd.read_csv('Overall_cleanedcomments.csv')
overall = overall[1:]
espn = pd.read_csv('espn_cleanedcomments.csv')
espn = espn[1:]
fb = pd.read_csv('fb_cleanedcomments.csv')
fb = fb[1:]
wnba =pd.read_csv('wnba_cleanedcomments.csv')
wnba = wnba[1:]
WF = pd.read_csv('WF_cleanedcomments.csv')
WF[1:]

WB = pd.read_csv('WB_cleanedcomments.csv')


def get_sentiments(data): 
    sentiment_scores = []
    label= []
    # Initialize the VADER sentiment intensity analyzer
    analyzer = SentimentIntensityAnalyzer()
    # Define a function to get sentiment scores
    for d in data: 
            comment = str(d)
            sentiment = analyzer.polarity_scores(comment)
            sentiment_scores.append(sentiment)

    for ss in sentiment_scores:
            #print(ss)
            if ss['compound'] > 0.05: 
                label.append('positive')
            elif ss['compound'] < -0.05: 
                label.append('negative')
            else: 
                label.append('neutral')
    return label

#get sentiment for each dataset 
o_s = get_sentiments(list(overall['0']))
# espn_s = get_sentiments(list(espn['0']))
# fb_s = get_sentiments(list(fb['0']))
# wnba_s= get_sentiments(list(wnba['0']))
# WF_s = get_sentiments(list(WF['0']))
WB_s = get_sentiments(list(WB['0']))

print("Counts for overall dataset:", Counter(o_s))
# print("Counts for espn dataset:", Counter(espn_s))
# print("Counts for fb dataset:", Counter(fb_s))
# print("Counts for wnba dataset:", Counter(wnba_s))
# print("Counts for WF dataset:", Counter(WF_s))
print("Counts for WF dataset:", Counter(WB_s))

def percentage(counter_sentiments): 
    total_counts = sum(Counter(counter_sentiments).values())
    percentage_dict = {item: (count / total_counts) * 100 for item, count in Counter(counter_sentiments).items()}
      # Create lists for sentiments and their corresponding percentages
    sentiments = list(percentage_dict.keys())
    percentages = list(percentage_dict.values())
    
    # Create a bar chart
    plt.bar(sentiments, percentages)
    plt.xlabel('Sentiment')
    plt.ylabel('Percentage')
    plt.title('Sentiment Distribution')
    
    # Display the percentages as text on top of the bars
    for sentiment, percentage in zip(sentiments, percentages):
        plt.text(sentiment, percentage, f'{percentage:.2f}%', ha='center', va='bottom')
    
    plt.show()

percentage(o_s)
# percentage(espn_s)
# percentage(fb_s)
# percentage(wnba_s)
# percentage(WF_s)
percentage(WB_s)


overall['sentiment'] = o_s
# espn['sentiment'] = espn_s
# fb['sentiment'] = fb_s
# wnba['sentiment'] = wnba_s
# WF['sentiment'] = WF_s
WB['sentiment'] = WB_s


#Split dataset 

opos_df = overall[overall['sentiment'] == 'positive']
oneg_df = overall[overall['sentiment'] == 'negative']
oneutral_df = overall[overall['sentiment'] == 'neutral']

opos_df.to_csv('opos_df.csv')
oneg_df.to_csv('oneg_df.csv')
oneutral_df.to_csv('oneutral_df.csv')


# espn_pos_df = espn[espn['sentiment'] == 'positive']
# espn_neg_df = espn[espn['sentiment'] == 'negative']
# espn_neutral_df = espn[espn['sentiment'] == 'neutral']

# espn_pos_df.to_csv('espn_posdf.csv')
# espn_neg_df.to_csv('espn_negdf.csv')
# espn_neutral_df.to_csv('espn_neutraldf.csv')

# fb_pos_df = fb[fb['sentiment'] == 'positive']
# fb_neg_df = fb[fb['sentiment'] == 'negative']
# fb_neutral_df = fb[fb['sentiment'] == 'neutral']

# fb_pos_df.to_csv('fb_pos_df.csv')
# fb_neg_df.to_csv('fb_neg_df.csv')
# fb_neutral_df.to_csv('fb_neutral_df.csv')

# wnba_pos_df = wnba[wnba['sentiment'] == 'positive']
# wnba_neg_df = wnba[wnba['sentiment'] == 'negative']
# wnba_neutral_df = wnba[wnba['sentiment'] == 'neutral']

# wnba_pos_df.to_csv('wnba_pos_df.csv')
# wnba_neg_df.to_csv('wnba_neg_df.csv')
# wnba_neutral_df.to_csv('wnba_neutral_df.csv')

wb_pos_df = WB[WB['sentiment'] == 'positive']
wb_neg_df = WB[WB['sentiment'] == 'negative']
wb_neutral_df = WB[WB['sentiment'] == 'neutral']

wb_pos_df.to_csv('wb_pos_df.csv')
wb_neg_df.to_csv('wb_neg_df.csv')
wb_neutral_df.to_csv('wb_neutral_df.csv')

# # Apply the sentiment analysis to your dataset
# s = get_sentiment_scores(list(data['0']))

# sentiment = [] 
# for ss in s: 
#     print(ss['compound'])
#     if ss['compound'] > 0.05: 
#         sentiment.append('positive')
#     elif ss['compound'] < -0.05: 
#         sentiment.append('negative')
#     else: 
#         sentiment.append('neutral')

# data['sentiment'] = sentiment


# # Use Counter to count the occurrences of each sentiment label
# sentiment_counts = Counter(sentiment)

# #split the dataset into different dataframe for sentiments 
# pos_df = data[data['sentiment'] == 'positive']
# neg_df = data[data['sentiment'] == 'negative']
# neutral_df = data[data['sentiment'] == 'neutral']

# pos_df.to_csv('pos_df.csv')
# neg_df.to_csv('neg_df.csv')
# neutral_df.to_csv('neu_df.csv')
# # Extract and assign sentiment labels
# data['compound_score'] = data['sentiment_scores'].apply(lambda x: x['compound'])
# data['sentiment_label'] = data['compound_score'].apply(lambda x: 'positive' if x >= 0.05 else 'negative' if x <= -0.05 else 'neutral')

# # Print or save the results
# print(data[['0', 'sentiment_label']])

# You can now analyze and label your text data with VADER sentiment analysis.
