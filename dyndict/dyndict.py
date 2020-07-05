import copy


class dyndict(dict):
    def __init__(self, dictionary:dict=dict(), add_num:bool=True):
        self.update(dictionary)
        self.add_num = add_num

    def __add__(self, b):
        return self._add_primitive(self, b)

    def overwrite(self, dictionary):
        self.dictionary = self._overwrite_primitive(self, dictionary)

    def _add_primitive(self, a, b):
        try:
            if isinstance(a, dict) or isinstance(b, dict):
                raise TypeError
            if (not self.add_num) and (isinstance(a, int) or isinstance(a, float)):
                raise TypeError
            return a + b
        except TypeError:
            if isinstance(a, dict) and isinstance(b, dict):
                c = copy.deepcopy(a)
                for i in b:
                    if i in c:
                        c[i] = self._add_primitive(c[i], b[i])
                    else:
                        c[i] = copy.deepcopy(b[i])
                return c
            elif isinstance(a, set) and isinstance(b, set):
                c = copy.deepcopy(a)
                c.update(b)
                return c
            elif isinstance(a, type(None)) and isinstance(b, type(None)):
                return None
            elif (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
                return b
            else:
                raise NotImplementedError

    def _overwrite_primitive(self, a, b):
        if type(a) != type(b):
            return copy.deepcopy(b)
        elif isinstance(a, dict):
            c = copy.deepcopy(a)
            for i in b:
                if i in c:
                    c[i] = self._overwrite_primitive(c[i], b[i])
                else:
                    c[i] = copy.deepcopy(b[i])
            return c
        else:
            return copy.deepcopy(b)
