
from data.DecisionTreeData import DecisionTreeData
import numpy as np
from sklearn.model_selection import train_test_split


class DessertData(DecisionTreeData):
    """
    The dessert data
    """
    def __init__(self, num_rows, noise=0.0, data=None):
        self._noise_level = noise
        self._num_rows = num_rows
        if data is None:
            num_features = 4
            feature_list = [[0, 1] for _ in range(num_features)]
            mesh = np.array(np.meshgrid(*feature_list))
            self._data = mesh.T.reshape(2 ** num_features, num_features)
        else:
            self._data = data

    def split(self, percentage):
        """
        Split the current data into a training set and a test set. If either set contains
        no data use an empty list.
        :param percentage:
        :return: tuple of training data and testing data
        """

        if percentage == 0.0:
            return DessertData(0, 0.0, []), self
        if percentage == 1.0:
            return self, DessertData(0, 0.0, [])
        train_data, test_data = train_test_split(self._data, train_size=percentage)
        train_rows = len(train_data)
        test_rows = len(test_data)
        return DessertData(train_rows, self._noise_level, train_data),\
               DessertData(test_rows, self._noise_level, test_data)

    def data(self):
        """
        Get the actual data as a list of lists
        :return: list of lists of the numerical data
        """
        return self._data