def vending_machine(snacks):
    """Cycles through list of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    index = -1
    def vend():
        nonlocal index
        if (index+1) in range(len(snacks)):
            index += 1
        else:
            index = 0
        return snacks[index]
    return vend
