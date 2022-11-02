import functools
from math import sqrt, floor


def NtoBinary(n):
    bits = []
    while n > 0:
        n, bit = divmod(n, 2)  # quotient and remainder of dividing n by 2
        bits.insert(0, bit)
    return bits


@functools.lru_cache(maxsize=1024)
def fibonacci(n):
    """An efficient algorithm for calculating the n-th element of the Fibonacci
    sequence; detailed descriptions of the algorithm can be found at:

        [1] http://bosker.wordpress.com/2011/04/29/the-worst-algorithm-in-the-world/
        [2] http://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
        [3] http://www.ics.uci.edu/~eppstein/161/960109.html

    """
    if n == 0:
        return 0

    a, b, c = 1, 0, 1
    # Our matrix has the form:
    # a b
    # b c
    bits = NtoBinary(n)
    for bit in bits:
        if bit:
            a, b = (a + c) * b, b * b + c * c
        else:
            a, b = a * a + b * b, (a + c) * b
        c = a + b
    return a


def isPalyndrome(n):
    string = str(n)
    return string == string[::-1]


def sieve(limit):
    """The Sieve of Eratosthenes """
    primes = list(range(2, limit + 1))
    end = int(sqrt(limit))
    length = len(primes)

    for i in range(0, end):
        if primes[i]:
            # you need to be very careful with this loop
            for j in range(i + primes[i], length, primes[i]):
                primes[j] = None
    return list(filter(None, primes))


def hailstone(n):
    """Counts the length of the hailstone sequence of given number n

       Details:
       http://en.wikipedia.org/wiki/Collatz_conjecture

    """
    c = 0  # I don't count the starting number
    while n > 1:
        if n % 2 == 1:
            # this is a visible improvement made possible by the fact that
            # the Collatz conjecture is defined as a parity sequence
            n = (3 * n + 1) / 2
        else:
            n /= 2
        c += 1
    return c


def binomial(n, k):
    """Calculates the binomial coefficient, using the efficient multiplicative
    formula:

    http://en.wikipedia.org/wiki/Binomial_coefficient#Multiplicative_formula

    """
    result = 1
    for i in range(1, k + 1):
        # separating the multiplication from the division allows us to avoid
        # some nasty floating point precision operations
        result *= n - (k - i)
        result //= i
    return result


def read_triangle(infile):
    """Reads a triangle of numbers from a file, as used in problems
       18 and 67.

    """
    f = open(infile, 'r')
    i = 0
    triangle = []
    for line in f:
        triangle.append([])
        tokens = line.split()
        for token in tokens:
            triangle[i].append(int(token))
        i += 1
    # we reverse the triangle to simplify the max sum algorithm
    return triangle[::-1]


def triangle_max_sum(triangle):
    """Calculates the maximum sum in a triangle of numbers, as in
    problems 18 and 67

       It does this efficiently, by iteratively calculating the maximum sum
       bottom-up.
    """
    for i in range(len(triangle) - 1):
        # we replace each line with the maximum sums below it
        new_line = []
        for j in range(len(triangle[i]) - 1):
            # each element of the new line is the maximum sum that can
            # be obtained from the elements below it
            new_line.append(max(triangle[i][j] + triangle[i + 1][j],
                                triangle[i][j + 1] + triangle[i + 1][j]))
        triangle[i + 1] = new_line
    # at the end, the maximum sum is at the top of the triangle
    # note that our triangle is upside-down, to simplofy the algorithm
    return triangle[len(triangle) - 1][0]


def toDigits(n):
    """Returns a list with the digits of given number n """
    digits = []
    while n > 0:
        qoutient = n / 10
        remainder = n % 10
        digits.append(remainder)
        n = qoutient
    return digits[::-1]


def divisors(n):
    """Returns all proper divisors of n"""
    divisors = [1] if n > 0 else []
    for i in range(2, floor(n/2)):
        if n % i == 0:
            divisors += [i, n//i]
    result = list(set(divisors))
    return result
