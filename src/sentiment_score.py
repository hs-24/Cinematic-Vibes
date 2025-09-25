#sentiment score python code goes here
# Do sentiment scoring
import pandas as pd

afinn = {}
# Create an empty dictionary
with open('AFINN-en-165.txt', encoding='utf-8') as word_scorer:
    for line in word_scorer:
        word, score = line.split('\t')
        afinn[word] = int(score)


# load the file
merged = pd.read_csv('merged_test.csv')

#Function to calculate movie review text sentiment score
def Sentiment_scorer(text, afinn):
    Sentiment_score = 0
    words = text.split()  # split the text into a list format and tokenise each word
    for word in words:
        word = word.lower()  # make the text lowercase
        if word in afinn:
            Sentiment_score += afinn[word]
    return Sentiment_score


# Create a Python list to contain the Sentiment Score
Sentiment_score = []

for text in merged['text']:
    score = Sentiment_scorer(text, afinn)
    Sentiment_score.append(score)

merged['Sentiment Score'] = Sentiment_score


# Name a function called and turn it into a column in the code to return its polarity value(Positive, Negative or Neutral)
def Sentimental_labelling(Sentiment_score):
   if sentiment_score > 0:
        return "Positive😀"
    elif sentiment_score < 0:
        return "Negative☹️"
    else:
        return "Neutral😐"


# Create a Sentimenal label for the various sentiments
merged['Sentimental label'] = merged['Sentiment Score'].apply(
    Sentimental_labelling)
