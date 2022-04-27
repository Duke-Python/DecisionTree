
from DessertData import DessertData
import learning.DecisionTree as DecisionTree

if __name__ == '__main__':
    num_rows = 100
    noise_level = 0.0
    train_percent = 1.0

    # clean dataset with feat and class
    data = DessertData(num_rows, noise_level)

    train_set, test_set = data.split(train_percent)
    tree = DecisionTree.DecisionTree(train_set)
    probability = tree.test(test_set)
