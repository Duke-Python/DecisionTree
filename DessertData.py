
import data.DecisionTreeData as DecisionTreeData


class DessertData(DecisionTreeData):
    """
    The dessert data
    """
    def __init__(self, num_rows, noise=0.0):
        self._noise_level = noise
        self._num_rows = num_rows
        pass

    def split(self, percentage):
        """
        Split the current data into a test set and a training set
        :param percentage:
        :return: tuple of testing data and training data
        """

        test_rows = int(percentage*self._num_rows)
        return DessertData(test_rows), DessertData(self._num_rows-test_rows)
