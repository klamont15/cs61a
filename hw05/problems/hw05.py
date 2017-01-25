def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    def other_pole(start, end):
        if start and end < 3:
            return start + end
        return abs(start - end)
    if n == 1:
        print_move(start, end)
    else:
        move_stack(n-1, start, other_pole(start,end))
        move_stack(1, start, end)
        move_stack(n-1, other_pole(start,end), end)


def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    return x[1]

def str_interval(x):
    """Return a string representation of interval x."""
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""
    upper1 = lower_bound(x) * lower_bound(y)
    upper2 = upper_bound(x) * upper_bound(y)
    lower1 = lower_bound(x) * upper_bound(y)
    lower2 = upper_bound(x) * lower_bound(y)
    return interval(min(lower1, lower2), max(upper1, upper2))

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""
    return interval(lower_bound(x)-upper_bound(y), upper_bound(x)-lower_bound(y))


def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""
    assert lower_bound(y) >= 0 or upper_bound(y) <= 0, 'Assertion Error'
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def check_par():
    """Return two intervals that give different results for parallel resistors.

    >>> r1, r2 = check_par()
    >>> x = par1(r1, r2)
    >>> y = par2(r1, r2)
    >>> lower_bound(x) != lower_bound(y) or upper_bound(x) != upper_bound(y)
    True
    """
    r1 = interval(3, 7) # Replace this line!
    r2 = interval(3, 7) # Replace this line!
    return r1, r2

def multiple_references_explanation():
    return """Assuming that the uncertainties are the upper and lower bounds r1 and r2 means there's four uncertain variables.
    Prior to div_interval calculationn par1 uses each upper and lower bound three times for a total of 12 uses of uncertainties
    whereas par2 uses each of the of uncertainties only once for a total of four uncertainties. Hence par2 is better"""

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    def f(x):
        return a*x*x + b*x + c
    upper_q = f(upper_bound(x))
    lower_q = f(lower_bound(x))
    extrema = f(-b/(2*a))
    if lower_bound(x) <= -b/(2*a) <= upper_bound(x):
        return interval(min(extrema, upper_q, lower_q), max(extrema, upper_q, lower_q))
    return interval(min(upper_q, lower_q), max(upper_q, lower_q))

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"
