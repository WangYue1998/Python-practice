# Sample function definitions, including a test driver

def convert(n, b):
    """Returns the base b representation of integer n as a string
       Requires: n and b are non-negative integers and 2 <= b <= 36"""

    result = ''           # initialize with no digits
    while (n != 0):
        x = n % b         # the remainder gives the next base-b 'digit'
        if x < 10:
            result = str(x) + result   # next digit is numeric
        else:             # use upper case letter for digit
            result = chr(55 + x) + result   # 'A' for 10, 'B' for 11, etc.
        n = n // b        # use the quotient for the next iteration

    if not result:
        result = '0'

    return result

def test():
    """test driver: executes some tests of convert"""

    OUT_TEMPL = '{}({}, {}) returned "{}"'
        
    n, b = 6, 2
    nstr1 = convert(11 - n, b)
    print(OUT_TEMPL.format('convert', 11 - n, b, nstr1))

    nstr2 = convert(125, b**4)
    print(OUT_TEMPL.format('convert', 125, b**4, nstr2))
     