import re
import string
import numpy as np

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

# initialize tokenizer
tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
en_stopwords = stopwords.words('english')  # load stopwords
stemmer = PorterStemmer()  # initialize stemmer


class NaiveBayse:
    def __init__(self):
        self.log_likelihood = {}
        self.log_prior = 0
        self.frequencies = {}

    def lookup(self, word, label):
        n = self.frequencies.get((word, label), 0)
        return n

    def fit(self, train_X, train_y):
        self.preprocess(train_X, train_y)
        vocab = set([pair[0] for pair in self.frequencies.keys()])
        V = len(vocab)
        N_pos = 0
        N_neg = 0
        for pair in self.frequencies.keys():
            if pair[1] > 0:
                N_pos += self.frequencies[pair]
            else:
                N_neg += self.frequencies[pair]
        D = len(train_y)
        D_pos = sum(train_y)
        D_neg = D - D_pos
        self.log_prior = np.log(D_pos) - np.log(D_neg)
        for word in vocab:
            freq_pos = self.lookup(word, 1)
            freq_neg = self.lookup(word, 0)

            p_w_pos = (freq_pos + 1) / (N_pos + V)
            p_w_neg = (freq_neg + 1) / (N_neg + V)

            self.log_likelihood[word] = np.log(p_w_pos) - np.log(p_w_neg)

    def preprocess(self, train_X, train_y):
        clean_texts = [self.preprocess_text(text) for text in train_X]
        y_list = list(np.squeeze(train_y))
        for label, tweet in zip(y_list, clean_texts):
            for word in tweet:
                pair = (word, label)
                self.frequencies[pair] = self.frequencies.get(pair, 0) + 1

    @staticmethod
    def preprocess_text(text):
        tweet = re.sub(r'RT[\s]+', '', text)  # remove retweet string
        tweet = re.sub(r'https?:\\.*[\r\n]*', '', tweet)  # remove hyperlinks
        tweet = re.sub(r'#', '', tweet)
        tweet_tokens = tokenizer.tokenize(tweet)
        clean_tweet = []
        for word in tweet_tokens:
            if (word not in en_stopwords and  # remove stop words
                    word not in string.punctuation):  # remove punctuations
                stem_word = stemmer.stem(word)  # stemming word
                clean_tweet.append(stem_word)

        return clean_tweet
