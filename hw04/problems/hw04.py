HW_SOURCE_FILE = 'hw04.py'

def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    return 1*g(n-1) + 2*g(n-2) + 3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    ##right now it's the infinite sum
    i = 1
    list_attempt = []
    def list_sum(alist):
        lsum = 0
        m = len(alist)
        while m > 3:
            alist = alist[1:]
            m -=1
        k = 0
        while k < m:
            lsum = lsum + alist[k]*(m-k)
            k +=1
        return lsum
    while i <= n:
        if i <= 3:
            list_attempt = list_attempt + [i]
        else:
            list_attempt = list_attempt + [list_sum(list_attempt)]
        i += 1
    return list_attempt[n-1]


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def pong(d):
        if d <= 6:
            return 0
        if d % 7 == 0 or has_seven(d):
            return 1 + pong(d-1)
        return pong(d-1)
    if n < 6:
        return n
    if pong(n-1) % 2 == 0:
        return pingpong(n-1) + 1
    return pingpong(n-1) - 1


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def max_power(n):
        i, num_twos = 1, -1
        while i < n:
            i = 2*i
            num_twos +=1
        return (2**num_twos)
    m = max_power(amount)
    def count_partitions(n, m):
        if n == 1 or m == 1:
            return 1
        elif m <= 0:
            return 0
        elif n < m:
            return count_partitions(n, m //2)
        elif n == m:
            return 1 + count_partitions(n, m//2)
        else:
            return count_partitions(n-m, m) + count_partitions(n, m//2)
    return count_partitions(amount, m)


###################
# Extra Questions #

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
