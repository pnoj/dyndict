import copy


class dyndict(dict):
    def __init__(self, dictionary:dict=dict(), refer_by=None):
        self.update(dictionary)
        self.refer_by = refer_by

    def __add__(self, b):
        return self._add_primitive(self, b)

    def overwrite(self, dictionary):
        self.dictionary = self._overwrite_primitive(self, dictionary)

    def _add_primitive(self, a, b):
        try:
            if isinstance(a, dict) or isinstance(b, dict):
                raise TypeError
            if isinstance(a, list) or isinstance(b, list):
                raise TypeError
            if isinstance(a, str) and isinstance(b, str):
                return b
            if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
                return b
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
            elif isinstance(a, list) and isinstance(b, list):
                c = copy.deepcopy(a)
                d = copy.deepcopy(b)
                e = c + d
                name_dict = dict()
                for i in range(0, len(e)):
                    if isinstance(e[i], dict) and 'name' in e[i]:
                        if e[i]['name'] in name_dict:
                            e[name_dict[e[i]['name']]] = self._add_primitive(e[name_dict[e[i]['name']]], e[i])
                        else:
                            name_dict[e[i]['name']] = i
                name_set = set()
                n = 0
                while n < len(e):
                    if isinstance(e[n], dict) and 'name' in e[n]:
                        if e[n]['name'] in name_set:
                            e.pop(n)
                        else:
                            name_set.add(e[n]['name'])
                            n += 1
                    else:
                        n += 1
                return e
            elif isinstance(a, type(None)) and isinstance(b, type(None)):
                return None
            else:
                print(type(a))
                print(type(b))
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
