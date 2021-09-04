"""
This is an example module for demonstrating doctest. The module supplies one function, arithmetic_sum().  Here is the __main__ test:

>>> arithmetic_sum(5)
15
"""

def arithmetic_sum(n):
    """Return the sum of n, an exact integer >= 0. Here are six tests in __main__.arithmetic_sum:

    >>> [arithmetic_sum(n) for n in range(6)]
    [0, 1, 3, 6, 10, 15]
    >>> arithmetic_sum(30)
    465
    >>> arithmetic_sum(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> arithmetic_sum(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> arithmetic_sum(30.0)
    465

    It must also not be ridiculously large:
    >>> arithmetic_sum(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 0
    factor = 1
    while factor <= n:
        result += factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)