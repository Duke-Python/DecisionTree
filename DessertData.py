
from data.DecisionTreeData import DecisionTreeData
import numpy as np
from sklearn.model_selection import train_test_split


class DessertData(DecisionTreeData):
    """
    The dessert data
    """
    def __init__(self, num_rows, noise=0.0, data=None):
        if num_rows < 0:
            raise ValueError("Num of rows >= 0")

        self._noise_level = noise
        self._num_rows = num_rows
        if data is None:
            num_features = 4
            feature_list = [[0, 1] for _ in range(num_features)]
            mesh = np.array(np.meshgrid(*feature_list))
            self._data = mesh.T.reshape(2 ** num_features, num_features)
            self._expand(self._num_rows)
#            self._define_classes()
        else:
            if num_rows != len(data):
                raise ValueError("Num of rows must match data")
            self._data = data

    def split(self, percentage):
        """
        Split the current data into a training set and a test set. If either set contains
        no data use an empty list.
        :param percentage:
        :return: tuple of training data and testing data
        """
        train_rows = percentage*self._num_rows
        if train_rows < 1:
            return DessertData(0, 0.0, []), self
        test_rows = self._num_rows - train_rows
        if test_rows < 1:
            return self, DessertData(0, 0.0, [])
        train_data, test_data = train_test_split(self._data, train_size=percentage)
        train_rows = len(train_data)
        test_rows = len(test_data)
        return DessertData(train_rows, self._noise_level, train_data),\
               DessertData(test_rows, self._noise_level, test_data)

    def _expand(self, num_rows):
        """
        Expand/contract data to num_rows by sampling the row numbers. If shrinking, then don't
        replace the row numbers.
        :param num_rows: Final number of rows in data
        """
        cur_rows = len(self._data)
        replace_rows = num_rows > cur_rows
        rows = np.random.choice(cur_rows, size=num_rows, replace=replace_rows)
        self._data = self._data[rows, :]

    def is_single_class(self):
        return False

    def get_max_info_gain(self):
        """
        Find feature with maximum information gain
        :return: feature
        """
        return None
