class Pascal:
    def __init__(self, list=None):
        self.p_list = list or []

    def __getitem__(self, item):
        return self.p_list[item - 1]

    def __setitem__(self, key, value):
        self.p_list[key - 1] = value

    def __str__(self):
        return self.p_list.__str__()
