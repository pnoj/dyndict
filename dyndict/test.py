import unittest
from dyndict import dyndict


class TestDynDict(unittest.TestCase):
    def setUp(self):
        self.dynd = dyndict()

    def tearDown(self):
        del self.dynd

    def test_adding_dictionary(self):
        self.dynd += {'a': 1}
        self.assertEqual(self.dynd, {'a': 1})
        self.dynd += {'b': 2}
        self.assertEqual(self.dynd, {'a': 1, 'b': 2})

    def test_adding_nested_dictionary(self):
        self.dynd += {'a': {}}
        self.assertEqual(self.dynd, {'a': {}})
        self.dynd += {'a': {'b': {}}}
        self.assertEqual(self.dynd, {'a': {'b': {}}})
        self.dynd += {'a': {'b': {'c': 3}}}
        self.assertEqual(self.dynd, {'a': {'b': {'c': 3}}})

    def test_adding_list(self):
        self.dynd += {'a': []}
        self.assertEqual(self.dynd, {'a': []})
        self.dynd += {'a': [1, 2, 3]}
        self.assertEqual(self.dynd, {'a': [1, 2, 3]})
        self.dynd += {'a': [{'b': 2}]}
        self.assertEqual(self.dynd, {'a': [1, 2, 3, {'b': 2}]})
        self.dynd += {'a': [{'b': 2}]}
        self.assertEqual(self.dynd, {'a': [1, 2, 3, {'b': 2}, {'b': 2}]})

    def test_adding_set(self):
        self.dynd += {'a': set()}
        self.assertEqual(self.dynd, {'a': set()})
        self.dynd += {'a': {1, 2, 3}}
        self.assertEqual(self.dynd, {'a': {1, 2, 3}})
        self.dynd += {'a': {1, 2, 3}}
        self.assertEqual(self.dynd, {'a': {1, 2, 3}})
        self.dynd += {'a': {4, 5, 6}}
        self.assertEqual(self.dynd, {'a': {1, 2, 3, 4, 5, 6}})

    def test_overwriting_int(self):
        self.dynd += {'a': -1}
        self.assertEqual(self.dynd, {'a': -1})
        self.dynd += {'a': 1}
        self.assertEqual(self.dynd, {'a': 1})

    def test_overwriting_string(self):
        self.dynd += {'a': 'abc'}
        self.assertEqual(self.dynd, {'a': 'abc'})
        self.dynd += {'a': 'def'}
        self.assertEqual(self.dynd, {'a': 'def'})

    def test_init_with_dict(self):
        self.dynd = dyndict({'a': 1})
        self.assertEqual(self.dynd, {'a': 1})

    def test_refer_by(self):
        self.dynd = dyndict(refer_by='name')
        self.dynd += {'list': [{'name': 'a', 'x': 0}, {'name': 'b', 'x': 1}]}
        self.assertEqual(self.dynd, {'list': [{'name': 'a', 'x': 0}, {'name': 'b', 'x': 1}]})
        self.dynd += {'list': [{'name': 'a', 'y': 2}, {'name': 'b', 'y': 3}]}
        self.assertEqual(self.dynd, {'list': [{'name': 'a', 'x': 0, 'y': 2}, {'name': 'b', 'x': 1, 'y': 3}]})


if __name__ == '__main__':
    unittest.main()
