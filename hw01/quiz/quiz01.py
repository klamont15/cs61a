def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """

    def factor_a(a, k):
        if a % k == 0:
            return True
    def factor_b(b, k):
        if b % k == 0:
            return True
    k = min(a,b)
    while k >1 and k <= min(a,b):
        if factor_a(a, k) and factor_b (b, k):
            factor = b // k
            b = factor
        k -= 1
    return b * a




def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    def has_digits (n,k):
        while n > 0:
            if n % 10 == k:
                return True
            n = n // 10

    sum = 0
    if has_digits (n,0):
        sum = 1 + sum
    if has_digits (n,1):
        sum = 1 + sum
    if has_digits (n,2):
        sum = 1 + sum
    if has_digits (n,3):
        sum = 1 + sum
    if has_digits (n,4):
        sum = 1 + sum
    if has_digits (n,5):
        sum = 1 + sum
    if has_digits (n,6):
        sum = 1 + sum
    if has_digits (n,7):
        sum = 1 + sum
    if has_digits (n,8):
        sum = 1 + sum
    if has_digits (n,9):
        sum = 1 + sum
    return sum
