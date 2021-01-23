import numpy as np


class NaiveBayse:
    def __init__(self):
        self.log_likelihood = {}
        self.log_prior = 0
        self.frequencies = {}

    def fit(self, frequencies, train_X, train_y):
        self.frequencies = frequencies
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
            pass
