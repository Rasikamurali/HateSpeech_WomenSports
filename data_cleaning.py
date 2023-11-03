import pandas as pd 
from matplotlib import pyplot as plt 
import seaborn as sns 
import nltk 
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import regex as re

nltk.download('stopwords')
stopwords = set(stopwords.words('english'))


def clean_comments(comments_list): 
    cleaned_comments = []
    for comment in comments_list: 
    #make everything lower case
        comment = comment.lower()
        words = comment.split()
        filtered_words = [word for word in words if word not in stopwords]
        cc = ' '.join(filtered_words)

        #remove punctuations 
        no_punkt = re.sub(r'[^\w\s]', '', cc)

        #remove emojis
        no_emojis = no_punkt.encode('ascii', 'ignore').decode('ascii')
        lemmatizer = WordNetLemmatizer()
        tokens = nltk.word_tokenize(no_emojis)
        lemmatized_sent = ' '.join([lemmatizer.lemmatize(token) for token in tokens])


        cleaned_comments.append(lemmatized_sent)
    return cleaned_comments



# #print(comments)

# cleaned_comments = []
# for comment in comments: 
#     #make everything lower case
#     comment = comment.lower()
#     #print(comment)

#     #remove stopwords 
#     words = comment.split()
#     filtered_words = [word for word in words if word.lower() not in stopwords]
#     cc = ' '.join(filtered_words)

#     #remove punctuations 
#     no_punkt = re.sub(r'[^\w\s]', '', cc)

#     #remove emojis
#     no_emojis = no_punkt.encode('ascii', 'ignore').decode('ascii')
#     lemmatizer = WordNetLemmatizer()
#     tokens = nltk.word_tokenize(no_emojis)
#     lemmatized_sent = ' '.join([lemmatizer.lemmatize(token) for token in tokens])


#     cleaned_comments.append(lemmatized_sent)
#     #print(lemmatized_sent)

# espn= pd.read_csv('espn_comments.csv')
# print(len(espn))
# football = pd.read_csv('fb_comments.csv')
# print(len(football))
# wnba  = pd.read_csv('wnba_comments.csv')
# WF = pd.read_csv('wf_comments.csv')

comments_df = pd.read_csv('combine_comments4.csv')
print(comments_df.head())
comments = list(comments_df['0'])

wb= pd.read_csv('WB_comments.csv')

overall_cc = clean_comments(comments)
# espn_cc = clean_comments(list(espn['0']))
# fb_cc = clean_comments(list(football['0']))
# wnba_cc = clean_comments(list(wnba['0']))
# WF_cc = clean_comments(list(WF['0']))
WB_cc = clean_comments(list(wb['0']))
def remove_duplicate_sentences(sentences):
    # Use a set to store unique sentences
    unique_sentences = set()

    # Iterate through the list and add non-duplicate sentences to the set
    for sentence in sentences:
        unique_sentences.add(sentence)

    # Convert the set back to a list
    unique_sentences_list = list(unique_sentences)

    return unique_sentences_list

overall_ccs = remove_duplicate_sentences(overall_cc)
overall_ccdf = pd.DataFrame(overall_ccs)
overall_ccdf.to_csv('Overall_cleanedcomments.csv')
# print(len(overall_ccdf))
# espn_ccs = remove_duplicate_sentences(espn_cc)
# espn_ccdf = pd.DataFrame(espn_ccs)
# espn_ccdf.to_csv('espn_cleanedcomments.csv')
# print(len(espn_ccdf))

# fb_ccs = remove_duplicate_sentences(fb_cc)
# fb_ccdf = pd.DataFrame(fb_ccs)
# fb_ccdf.to_csv('fb_cleanedcomments.csv')

# wnba_ccs = remove_duplicate_sentences(wnba_cc)
# wnba_ccdf = pd.DataFrame(wnba_ccs)
# wnba_ccdf.to_csv('wnba_cleanedcomments.csv')

WB_ccs = remove_duplicate_sentences(WB_cc)
WB_ccdf = pd.DataFrame(WB_ccs)
WB_ccdf.to_csv('WB_cleanedcomments.csv')
#drop duplicates 
# Use a set to store unique sentences
# unique_sentences = set()

# # Iterate through the list and add non-duplicate sentences to the set
# for sentence in cleaned_comments:
#     unique_sentences.add(sentence)

# # Convert the set back to a list if needed
# unique_sentences_list = list(unique_sentences)

# # Print the unique sentences
# cleaned_comments_df = pd.DataFrame(unique_sentences_list)
# cleaned_comments_df.to_csv('cleaned_comments2.csv')

# print(len(cleaned_comments_df))

