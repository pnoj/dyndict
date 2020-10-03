import copy

class dyndict(dict):
    def __init__(self, dictionary: dict=dict(), refer_by=None):
        """
        Creates a new dyndict from a dict instance.
        """
        self.update(dictionary)
        self.refer_by = refer_by

    def __add__(self, b: dict):
        """
        Adds another dictionary to the current dyndict.
        """
        return self._add_primitive(self, b)

    def overwrite(self, dictionary):
        """
        Overwrites the current dyndict to a new dictionary.
        """
        self.dictionary = self._overwrite_primitive(self, dictionary)

    def _add_dict(self, a: dict, b: dict):
        """
        Adds two dicts according to dyndict rules.
        """
        a = copy.deepcopy(a)
        for key in b:
            if key in a:
                a[key] = self._add_primitive(a[key], b[key])
            else:
                a[key] = copy.deepcopy(b[key])
        return a

    def _add_list(self, a: list, b: list):
        """
        Adds two lists according to dyndict rules.
        """
        sum_list = copy.deepcopy(a) + copy.deepcopy(b)
        name_dict = dict()
        for index, elem in enumerate(sum_list):
            if isinstance(elem, dict) and 'name' in elem:
                name = elem['name']
                if name in name_dict:
                    name_idx = name_dict[name]
                    sum_list[name_idx] = self._add_primitive(sum_list[name_idx], elem)
                else:
                    name_dict[name] = index
        name_set = set()
        i = 0
        while i < len(sum_list):
            elem = sum_list[i]
            if isinstance(elem, dict) and 'name' in elem:
                name = elem['name']
                if name in name_set:
                    sum_list.pop(i)
                else:
                    name_set.add(name)
                    i += 1
            else:
                i += 1
        return sum_list

    def _add_set(self, a: set, b: set):
        """
        Adds two sets according to dyndict rules.
        """
        a = copy.deepcopy(a)
        a.update(b)
        return a

    def _add_primitive(self, a, b):
        """
        Adds two arbitrary object instances.
        Will originally be called by __add__ for itself and another dictionary.
        """
        if isinstance(a, dict) or isinstance(b, dict):
            return self._add_dict(a, b)
        elif isinstance(a, list) or isinstance(b, list):
            return self._add_list(a, b)
        elif isinstance(a, set) or isinstance(b, set):
            return self._add_set(a, b)
        elif isinstance(a, str) or isinstance(b, str):
            return b
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return b
        elif a is None and b is None:
            return None
        else:
            try:
                return a + b
            except TypeError:
                print(type(a))
                print(type(b))
                raise NotImplementedError

    def _overwrite_primitive(self, a, b):
        """
        Overwrites two arbitrary object instances.
        Will be called by overwrite.
        """
        if type(a) != type(b):
            return copy.deepcopy(b)
        elif isinstance(a, dict):
            a = copy.deepcopy(a)
            for key in b:
                if key in a:
                    a[key] = self._overwrite_primitive(a[key], b[key])
                else:
                    a[i] = copy.deepcopy(b[key])
            return a
        else:
            return copy.deepcopy(b)
