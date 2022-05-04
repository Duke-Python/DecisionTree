from learning.Node import Node


class LeafNode(Node):
    """
    Contain information related to a leaf tree node. Need attribute.
    """
    def __init__(self, class_attr):
        super().__init__(class_attr)
