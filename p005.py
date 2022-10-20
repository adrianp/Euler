from functools import reduce
from math import floor, log, sqrt
import sys

from euler_util import sieve


def naive(k):
    primes = sieve(k)
    powers = {p: 1 for p in primes}
    for i in range(1, k+1):
        j = i
        if i not in primes:
            for p in primes:
                power = 0
                while j % p == 0:
                    power += 1
                    j /= p
                powers[p] = max(power, powers[p])
    print(reduce(lambda v, e: v*(e[0]**e[1]), powers.items(), 1))


def main(nr):
    result, check = 1, True
    limit = sqrt(nr)
    primes = sieve(nr)
    a = [1] * nr
    for i in range(len(primes)):
        if check:
            if primes[i] <= limit:
                a[i] = floor(log(nr) / log(primes[i]))
            else:
                check = False
        result *= primes[i] ** a[i]
    print(result)
    return 0


if __name__ == "__main__":
    naive(20)
    main(20)
    sys.exit(0)
