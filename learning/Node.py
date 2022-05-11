

class Node:
    """
    Contain information related to a decision/leaf tree node. Need attribute. For decision nodes
    the attribute is a feature, for a leaf node the attribute is a leaf.
    """
    def __init__(self, attribute) -> None:
        self._attribute = attribute
