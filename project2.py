"""
Basic Sentiment Analysis

The goal of this project is to familiarize ourselves with the processing of text files using Python (without importing specialized libraries for text parsing) and to practice working with Python data types, such as strings, lists, sets, dictionaries, and files.

Download the text of the ebook The Hound of the Baskervilles by A. Conan Doyle from our course website, along with two files: positivesentimentwords.txt and negativesentimentwords.txt.

We want to analyze the sentiment of the text on the sentence level. That is, we want to classify each sentence in this text as having either positive, neutral, or negative sentiment. The following three sentences illustrate each sentiment type. For example,

I am so excited about my new car. (Positive sentiment)

I feel tired and moody today. (Negative sentiment)

There is parked car on the street. (Neutral sentiment)

To aid us in deciding which words carry positive, neutral, or negative sentiment, we will consult the two files  positivesentimentwords.txt and negativesentimentwords.txt. Each of these files contains a list of words that are generally associated with positive/negative sentiment.

The classification of each sentence as being positive, neutral, or negative is based on the following assessment. If more words in a sentence carry the positive sentiment than negative, we will classify that sentence as having a positive sentiment. If the number of positive and negative words in a sentence is equal, we will classify that sentence as neutral. Otherwise, the sentence is classified as having a negative sentiment.

Upon completion, your code should print sentence counts for each sentiment type:

Positive:
Negative:
Neutral :
"""


def read_in_sentiment_words(s):
    with open(s,'r',errors = 'ignore') as f:
        L = []
        for line in f:
            line = line.replace("\n","")
            L.append(line)
    return L

def word_sentiment():
    pcnt = 0
    ncnt = 0
    neutcnt = 0
    S = ("/Users/sydneyn/Downloads/thehoundofthebaskervilles.txt") #["My name is Danko and I am good at math", "Today is Tuesday and it's rainy"]
    P = read_in_sentiment_words("/Users/sydneyn/Downloads/positivesentimentwords.txt")  # ["good","sunny"]
    N = read_in_sentiment_words("/Users/sydneyn/Downloads/negativesentimentwords.txt")  # ["rainy" , "bad"]
    with open(S, 'r', errors='ignore') as f:
        sent = f.read()  # read in the entire book at once and assign it to variable text
        sent = sent.lower()
        sent = sent.replace("?", ".")
        sent = sent.replace("!", ".")
    S = sent.split(".")
    for sentence in S:
            words = sentence.split(" ")
            interP = len(set(words).intersection(set(P)))
            interN = len(set(words).intersection(set(N)))
            if interP > interN:
                pcnt += 1
            elif interP < interN:
                ncnt += 1
            else:
                neutcnt += 1
    print(pcnt,ncnt,neutcnt)

def testing():
    P = read_in_sentiment_words(("/Users/sydneyn/Downloads/positivesentimentwords.txt"))
    print(P)


def main():
    word_sentiment()



main()