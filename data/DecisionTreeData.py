
class DecisionTreeData:

    def split(self, percentage):
        raise NotImplementedError

    def get_max_info_gain(self):
        raise NotImplementedError

    def is_single_class(self):
        raise NotImplementedError
