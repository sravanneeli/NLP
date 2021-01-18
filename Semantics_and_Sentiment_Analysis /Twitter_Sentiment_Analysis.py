import re
import numpy as np
import string
from nltk.corpus import stopwords, twitter_samples
from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer
from Models.Logistic_Regression import LogisticRegression
from sklearn.model_selection import train_test_split

np.random.seed(1)

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


def load_raw_tweets():
    all_positive_tweets = twitter_samples.strings('positive_tweets.json')
    all_negative_tweets = twitter_samples.strings('negative_tweets.json')
    return all_positive_tweets, all_negative_tweets


def get_freq(labels, tweets):
    freq = {}
    y_list = list(np.squeeze(labels))
    for label, tweet in zip(y_list, tweets):
        for word in tweet:
            pair = (word, label)
            freq[pair] = freq.get(pair, 0) + 1

    return freq


def build_feature_vectors(freq, tweets, labels):
    data = []
    y_list = list(np.squeeze(labels))

    for label, tweet in zip(y_list, tweets):
        pos = 0
        neg = 0
        for word in tweet:
            if (word, 1) in freq:
                pos += freq[(word, 1)]
            if (word, 0) in freq:
                neg += freq[(word, 0)]
        data.append([pos, neg, label])

    return data


def train_model(data):
    X, y = data[:, :-1], data[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)
    lr = LogisticRegression(alpha=1e-09, num_iter=1500)
    J, theta = lr.fit(X_train, y_train)
    print(J, theta)


def main():
    raw_pos_tweets, raw_neg_tweets = load_raw_tweets()  # load tweets from nltk
    tweets = raw_pos_tweets + raw_neg_tweets  # all tweets
    # positive and negative labels
    labels = np.append(np.ones((len(raw_pos_tweets))), np.zeros((len(raw_neg_tweets))))
    clean_tweets = [preprocess_tweet(tweet) for tweet in tweets]
    freq = get_freq(labels, clean_tweets)  # get frequency dictionary of all words/vocab
    data = np.array(build_feature_vectors(freq, clean_tweets, labels))
    train_model(data)


if __name__ == '__main__':
    main()
