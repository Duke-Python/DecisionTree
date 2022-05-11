import numpy as np
from sklearn.model_selection import train_test_split

from data.DecisionTreeData import DecisionTreeData
from data.Feature import Feature


class DessertData(DecisionTreeData):
    """
    The dessert data. Numerical data is stored as a list of lists. Features is a dictionary using
    feature as a key and the column as the value.
    """
    def __init__(self, num_rows: int, noise=0.0, data: tuple[list, dict] = None) -> None:
        """
        Initialize dessert data
        :param num_rows:
        :param noise:
        :param data: tuple of data and features
        """
        if num_rows < 0:
            raise ValueError("Num of rows >= 0")

        self._noise_level = noise
        self._num_rows = num_rows
        if data is None:
            num_features = 4
            feature_list = [[0, 1] for _ in range(num_features)]
            mesh = np.array(np.meshgrid(*feature_list))
            self._data = mesh.T.reshape(2 ** num_features, num_features)
            self._data = self._expand(self._num_rows, self._data)
            self._features = self._define_features()
#            self._define_classes()
        else:
            self._data, self._features = data
            if num_rows != len(self._data):
                raise ValueError("Num of rows must match data")
            if len(self._features) != len(self._data[0]):
                raise ValueError("Num of features must match data")

    @staticmethod
    def _define_features() -> dict:
        """
        Define the features of this data set. Make static to allow it to be called from __init__
        :return: feature dictionary
        """
        feature_descriptions = ["Eaten", "Hungry", "Healthy", "Tasty"]
        values = [{"yes": 1, "no": 0}, {"yes": 1, "no": 0}, {"yes": 1, "no": 0}]
        ret_dict = {}
        for col_num, (description, value) in enumerate(zip(feature_descriptions, values)):
            ret_dict[Feature(description, value)] = col_num

        return ret_dict

    def split(self, percentage: float) -> tuple[DecisionTreeData, DecisionTreeData]:
        """
        Split the current data into a training set and a test set. If either set contains
        no data use an empty list.
        :param percentage:
        :return: tuple of training data and testing data
        """
        train_rows = percentage*self._num_rows
        if train_rows < 1:
            return DessertData(0, 0.0, ([], {})), self
        test_rows = self._num_rows - train_rows
        if test_rows < 1:
            return self, DessertData(0, 0.0, ([], {}))
        train_data, test_data = train_test_split(self._data, train_size=percentage)
        train_rows = len(train_data)
        test_rows = len(test_data)
        return DessertData(train_rows, self._noise_level, train_data),\
               DessertData(test_rows, self._noise_level, test_data)

    @staticmethod
    def _expand(num_rows, data) -> list:
        """
        Expand/contract data to num_rows by sampling the row numbers. If shrinking, then don't
        replace the row numbers. Make static to enable calling from __init__
        :param num_rows: Final number of rows in data
        :param data: list of lists of numerical data
        """
        cur_rows = len(data)
        replace_rows = num_rows > cur_rows
        rows = np.random.choice(cur_rows, size=num_rows, replace=replace_rows)
        return data[rows, :]

    def is_single_class(self) -> bool:
        test_value = self._data[0][-1]
        class_data = [row[-1] for row in self._data]
        return all([elem == test_value for elem in class_data])

    def get_max_info_gain(self) -> list:
        """
        Find feature with maximum information gain
        :return: feature
        """
        return list(self._features.keys())[0]

    def remove_feature(self, feature: Feature):
        pass
