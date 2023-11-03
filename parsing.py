import pandas as pd 
import json

espn_women_data = pd.read_csv('espn_women_comments7.csv')
football_comments = pd.read_csv('womens_football_comments7.csv')
wnba_comments  = pd.read_csv('wnba_comments2.csv')
WomensFootball_comments = pd.read_csv('WF_comments1.csv')
WomensBasketball_comments = pd.read_csv('WB_comments.csv')
#print(espn_women_data.head())
#print(WomensFootball_comments.columns())
combine_comments = [item for sublist in 
                    [list(espn_women_data['comments']), list(football_comments['comments']), 
                     list(wnba_comments['comments']), list(WomensFootball_comments['comments']),
                     list(WomensBasketball_comments['comments'])] 
                    for item in sublist]

print(len(combine_comments))
# Initialize a new list for individual sentences

def parsing(data): 
    sentences_list = []

    # Split the original list into individual sentences
    for string in data:
        sentences = string.split(', ')
        sentences_list.extend(sentences)

    print(len(sentences_list))
    return sentences_list

overall_comments = parsing(combine_comments)
comments_df = pd.DataFrame(overall_comments)
comments_df.to_csv('combine_comments4.csv')

espn_comments = parsing(list(espn_women_data['comments']))
espn_df = pd.DataFrame(espn_comments)
espn_df.to_csv('espn_comments.csv')


fb_comments = parsing(list(football_comments['comments']))
fb_df = pd.DataFrame(fb_comments)
fb_df.to_csv('fb_comments.csv')

wnba_comments = parsing(list(wnba_comments['comments']))
wnba_df = pd.DataFrame(wnba_comments)
wnba_df.to_csv('wnba_comments.csv')

WF_comments = parsing(list(WomensFootball_comments['comments']))
WF_df = pd.DataFrame(WF_comments)
WF_df.to_csv('wf_comments.csv')

WB_comments = parsing(list(WomensBasketball_comments['comments']))
WB_df = pd.DataFrame(WB_comments)
WB_df.to_csv('wb_comments.csv')

