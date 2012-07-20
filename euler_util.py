from math import sqrt


def NtoBinary(n):
    bits = []
    while n > 0:
        n, bit = divmod(n, 2)  # quotient and remainder of dividing n by 2
        bits.append(bit)
    bits.reverse()
    return bits


# The algorithm to generate the n-th element of the Fibonacci sequence is
# described in detail on the following pages:
# [1] http://bosker.wordpress.com/2011/04/29/the-worst-algorithm-in-the-world/
# [2] http://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
# [3] http://www.ics.uci.edu/~eppstein/161/960109.html
def fibonacci(n):
    assert n >= 0
    a, b, c = 1, 0, 1
    #Our matrix has the form:
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
    return filter(None, primes)


def hailstone(n):
    """Counts the length of the hailstone sequence of given number n

       Details:
       http://en.wikipedia.org/wiki/Collatz_conjecture

    """
    c = 0  # I don't count the starting number
    while n > 1:
        if n % 2 == 1:
            # this is a visible improvement made possible by the fact that
            # The Collatz conjecture is defined as a parity sequence
            n = (3 * n + 1) / 2
        else:
            n /= 2
        c += 1
    return c
