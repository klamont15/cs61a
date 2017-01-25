from lab03 import *

def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

def product(n, term):
    """Return the product of the first n terms in a sequence.

    n    -- a positive integer
    term -- a function that takes one argument

    >>> product(3, identity) # 1 * 2 * 3
    6
    >>> product(5, identity) # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)   # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)   # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    """
    k = 1
    a = 1
    while k <= n:
        term (k)
        a = a * term (k)
        k +=1
    return a


# The identity function, defined using a lambda expression!
identity = lambda k: k

def factorial(n):
    """Return n factorial for n >= 0 by calling product.

    >>> factorial(4)
    24
    >>> factorial(6)
    720
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'factorial', ['Recursion', 'For', 'While'])
    True
    """

    return product(n, identity)

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    while x > 0:
        x, y = x // 10, 10*y + x % 10
    return y == n

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        if i == n:
            print (n)
            return
        print (i)
        counter(i+1)
    counter(1)

def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    def multiplication(a,b):
        if a == 0:
            return 0
        else:
            return b + multiplication(a-1, b)
    return multiplication(a,b) + c

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def factor(a,b):
        if b == 1:
            return True
        elif a % b == 0:
            return False
        return factor(a, b-1)
    return factor(n,n-1)



def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    if n = 1:
        return odd_term(1) + even_term(2)
    else:

        return interleaved_sum

def digit(k, n):
    counter = 0
    while n > 0:
        if n % 10 == k:
            counter = counter + 1
        n = n // 10
    return counter

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    a, b = 1, 9
    tens = 0
    while a != b:
        c = digit(a, n)
        d = digit(b, n)
        if c and d:
            tens = tens + c*d
        a += 1
        b -= 1
    if a == b:
        m = digit(a, n)
        if m == 0 or m == 1:
            tens = tens
        else:
            tens = tens + 2*(m-1)
    return tens
