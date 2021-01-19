import numpy as np
from Models.utils import sigmoid


class LogisticRegression:
    def __init__(self, alpha=1e-8, num_iter=1000):
        self.theta = None
        self.alpha = alpha
        self.num_iter = num_iter
        self.cost_hist = []
        self.m = 0
        self.n = 0

    def cost_function(self, h, y):
        J = -1. / self.m * (np.dot(y.transpose(), np.log(h)) +
                            np.dot((1 - y).transpose(), np.log(1 - h)))
        self.cost_hist.append(J)

    def fit(self, X, y):
        self.m, self.n = X.shape
        y = y.reshape(self.m, 1)
        self.theta = np.zeros((self.n + 1, 1))  # theta parameter matrix
        X = np.append(np.ones((self.m, 1)), X, axis=1)  # Input Feature Matrix with bias
        for i in range(self.num_iter):
            z = np.dot(X, self.theta)  # z = X * theta.T
            h = sigmoid(z)  # sigmoid of input
            self.cost_function(h, y)
            self.theta -= (self.alpha / self.m) * np.dot(X.transpose(), (h - y))

        return float(self.cost_hist[-1]), self.theta

    def predict(self, X):
        X = np.append(np.ones((len(X), 1)), X, axis=1)  # Input Feature Matrix with bias
        y_predicted = np.squeeze(sigmoid(np.dot(X, self.theta)))
        y_predicted = [1 if x > 0.5 else 0 for x in y_predicted]
        return y_predicted
