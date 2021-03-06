def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    if n == -1:
        return
    yield n
    yield from countdown(n-1)

def trap(s, k):
    """Return a generator that yields the first K values in iterable S,
    but raises a ValueError exception if any more values are requested.

    >>> t = trap([3, 2, 1], 2)
    >>> next(t)
    3
    >>> next(t)
    2
    >>> next(t)
    ValueError
    >>> list(trap(range(5), 5))
    ValueError
    """
    assert len(s) >= k
    for elem in range(k+1):
        if elem == k:
            raise ValueError
        yield s[elem]



def repeated(t, k):
    """Return the first value in iterable T that appears K times in a row.

    >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    >>> repeated(trap(s, 7), 2)
    4
    >>> repeated(trap(s, 10), 3)
    5
    >>> print(repeated([4, None, None, None], 3))
    None
    """
    assert k > 1
    t = iter(t)
    prev = next(t)
    while t:
        try:
            s = next(t)
            if s == prev:
                k -= 1
            if k == 1:
                return s
            prev = s
        except StopIteration or ValueError:
            return None



def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    if n == 1:
        yield n
    elif n % 2 == 0:
        yield n
        yield from hailstone(n//2)
    else:
        yield n
        yield from hailstone(3*n+1)
