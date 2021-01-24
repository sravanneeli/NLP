import re
import string

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
