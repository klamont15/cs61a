def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    def factor(a, k):
        if a % k == 0:
            return True
    k = min(a,b)
    while k >=1 and k <= min(a,b):
        if factor(a, k) and factor(b, k):
            return k
        k -= 1

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print (int(n))
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n/2)
    else:
        return 1 + hailstone(3*n + 1)
