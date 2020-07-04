import copy

class dyndict(dict):
    def __add__(self, b):
        return self._add_primitive(self, b)

    def overwrite(self, dictionary):
        self.dictionary = self._overwrite_primitive(self, dictionary)

    def _add_primitive(self, a, b):
        try:
            if isinstance(a, dict):
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
                c.update(a)
                return c
            elif isinstance(a, None) and isinstance(b, None):
                return None
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
