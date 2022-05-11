from data import Feature


class TreeData:
    pass


class DecisionTreeData(TreeData):

    def split(self, percentage) -> tuple[TreeData, TreeData]:
        raise NotImplementedError

    def get_max_info_gain(self) -> Feature:
        raise NotImplementedError

    def is_single_class(self) -> bool:
        raise NotImplementedError
