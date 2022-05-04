from learning.Node import Node


class DecisionNode(Node):
    """
    Contain information related to a decision tree node. Need attribute, edges, and children.
    """
    class Children:
        """
        Children are stored in a dictionary whose key is the edge and value is the child node
        """
        def __init__(self):
            self._children = {}

        def append(self, edge, child_node):
            self._children[edge] = child_node

    def __init__(self, feature):
        self._feature = super().__init__(feature.attribute)
        self._children = self.Children()

    def add_child(self, node, edge):
        self._children.append(node, edge)
