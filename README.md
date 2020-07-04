## DynDict

![Python test](https://github.com/hillcrestpaul0719/dyndict/workflows/Python%20test/badge.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/dyndict)

Dynamic Dictionary class for Python adds support for add operation for dictionary classes.

#### Demo

```python
Python 3.8.3 (default, May 17 2020, 18:15:42) 
[GCC 10.1.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from dyndict import dyndict
>>> dyn = dyndict()
>>> dyn
{}
>>> dyn += {'a': 1}
>>> dyn
{'a': 1}
>>> dyn += {'b': 1}
>>> dyn
{'a': 1, 'b': 1}
>>> dyn += {'b': 1}
>>> dyn
{'a': 1, 'b': 2}
>>> dyn += {'list': []}
>>> dyn
{'a': 1, 'b': 2, 'list': []}
>>> dyn += {'list': [1, 2, 3]}
>>> dyn
{'a': 1, 'b': 2, 'list': [1, 2, 3]}
>>> dyn += {'list': [{'z': 26}]}
>>> dyn
{'a': 1, 'b': 2, 'list': [1, 2, 3, {'z': 26}]}
>>> dyn['a']
1
>>> dyn['list'][3]
{'z': 26}
```

### Installation

```bash
pip install dyndict
```
