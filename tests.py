"""
This file contains tests
>>> 1+1
2
"""
def oneplusone():
    """
    >>> 1+1
    2
    """
    pass
def _test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == "__main__":
    _test()
