from learning.LeafNode import LeafNode
from learning.DecisionNode import DecisionNode
from learning.Node import Node


class DecisionTree:

    def __init__(self, train_data) -> None:
        self._root = self._id3(train_data)

    def test(self, data) -> float:
        """
        Test the decision tree
        :param data: object used to test the decision tree
        :return: percentage of correct classification
        """

        return 0.0

    def _id3(self, data) -> Node:
        if data.is_single_class():
            return LeafNode(data.class_attribute)
        feature = data.get_max_info_gain()
        node = DecisionNode(feature)
        new_data = data.remove_feature(feature)
        for value in feature.values:
            node.add_child(node=self._id3(new_data), edge=value)

        return node
