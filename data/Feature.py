class Feature:
    """
    A feature contains a description and a dictionary of possible values. The value dictionary
    contains the value description and numerical value. Allow this object to be a key.
    """
    def __init__(self, attribute, values) -> None:
        self._attribute = attribute
        self._lower_attr = attribute.lower()
        self._values = values

    def __hash__(self) -> int:
        return hash(self._lower_attr)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Feature):
            return False
        return self._lower_attr == other._lower_attr

    @property
    def attribute(self) -> str:
        return self._attribute

    @property
    def values(self) -> list:
        return list(self._values.keys())
