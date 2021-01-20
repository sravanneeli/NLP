import numpy as np
from nltk.corpus import twitter_samples
from sklearn.model_selection import train_test_split
from utils import preprocess_tweet
from Models.Logistic_Regression import LogisticRegression

np.random.seed(1)


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


def build_input_data(freq, tweets, labels):
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


def extract_features(tweets, freq):
    x = np.zeros((len(tweets), 2))
    for i, tweet in enumerate(tweets):
        for word in preprocess_tweet(tweet):
            x[i, 0] += freq.get((word, 1.0), 0)
            x[i, 1] += freq.get((word, 0.0), 0)
    return x


def accuracy(y_test, y_predicted):
    return (y_test == np.squeeze(y_predicted)).sum() / len(y_predicted)


def train_model(data):
    X, y = data[:, :-1], data[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)
    lr = LogisticRegression(alpha=1e-09, num_iter=1500)
    J, theta = lr.fit(X_train, y_train)
    print(f"Loss and parameters after training with Logistic Regression are {J}, {theta}")
    y_predicted = lr.predict(X_test)
    acc = accuracy(y_test, y_predicted)
    print(f"Logistic regression model's accuracy = {acc:.4f}")
    return lr


def test_raw_tweet(tweets, freq, model):
    x = extract_features(tweets, freq)
    predicted = model.predict(x)
    return predicted


def main():
    raw_pos_tweets, raw_neg_tweets = load_raw_tweets()  # load tweets from nltk
    tweets = raw_pos_tweets + raw_neg_tweets  # all tweets
    # positive and negative labels
    labels = np.append(np.ones((len(raw_pos_tweets))), np.zeros((len(raw_neg_tweets))))
    clean_tweets = [preprocess_tweet(tweet) for tweet in tweets]
    freq = get_freq(labels, clean_tweets)  # get frequency dictionary of all words/vocab
    data = np.array(build_input_data(freq, clean_tweets, labels))
    model = train_model(data)
    test_tweets = ["@sravan I am feeling very happy today because I completed my work!!!!!", "I am sad"]
    labels_pred = test_raw_tweet(test_tweets, freq, model)
    print(labels_pred)


if __name__ == '__main__':
    main()
