from math import sqrt
import sys


def main(n):
    factor = 1

    # while this is not necessary, checking now for division by 2 means we
    # won't have to check for even factors lately
    if n % 2 == 0:
        factor = 2
        n /= 2
        while n % 2 == 0:
            n /= 2

    current = 3
    maxval = sqrt(n)
    while n > 1 and current <= maxval:
        if n % current == 0:
            factor = current
            n /= current
            while n % current == 0:
                n /= current
            maxval = sqrt(n)
        current += 2  # we already checked for even factors
    if n == 1:
        print factor
    else:
        print n  # is a prime itself

    return 0

if __name__ == "__main__":
    sys.exit(main(600851475143))
