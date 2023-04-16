import numpy as np
from collections import Counter

def euclidean_distance(x1, x2):

    distance = np.sqrt(np. sum((x1-x2)**2))
    return distance


class KNN():

    def __init__(self, k=3):

        self.k = k

    def fit(self, X, y):

        self.X_train = X
        self.y_train = y

    def predict(self, X):

        predictions = [self._predict(x) for x in X]
        return predictions

    def _predict(self, x):

        # Calculate the distances of all the data points in the training dataset to the new point
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]

        #  Find the indices of the first k closest points to the new data point
        k_indices = np.argsort(distances)[:self.k]
        labels = [self.y_train[i] for i in k_indices]

        # Count the labels with majority Vote
        majority_vote = Counter(labels).most_common()
        return majority_vote[0][0]