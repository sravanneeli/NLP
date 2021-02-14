import re
import string
import numpy as np
import pandas as pd

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

# initialize tokenizer
tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
en_stopwords = stopwords.words('english')  # load stopwords
stemmer = PorterStemmer()  # initialize stemmer


def preprocess_tweet(tweet):
    tweet = re.sub(r'RT[\s]+', '', tweet)  # remove retweet string
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)  # remove hyperlinks
    tweet = re.sub(r'#', '', tweet)
    tweet_tokens = tokenizer.tokenize(tweet)
    clean_tweet = []
    for word in tweet_tokens:
        if (word not in en_stopwords and  # remove stop words
                word not in string.punctuation):  # remove punctuations
            stem_word = stemmer.stem(word)  # stemming word
            clean_tweet.append(stem_word)

    return clean_tweet

def get_dict(file_name):
    """
    This function returns the english to french dictionary given a file where the each column corresponds to a word.
    Check out the files this function takes in your workspace.
    """
    my_file = pd.read_csv(file_name, delimiter=' ')
    etof = {}  # the english to french dictionary to be returned
    for i in range(len(my_file)):
        # indexing into the rows.
        en = my_file.loc[i][0]
        fr = my_file.loc[i][1]
        etof[en] = fr

    return etof

def cosine_similarity(A, B):
    '''
    Input:
        A: a numpy array which corresponds to a word vector
        B: A numpy array which corresponds to a word vector
    Output:
        cos: numerical number representing the cosine similarity between A and B.
    '''
    cos = -10
    dot = np.dot(A, B)
    norma = np.linalg.norm(A)
    normb = np.linalg.norm(B)
    cos = dot / (norma * normb)
