from math import ceil, sqrt, gcd
import sys


def naive(ssum):
    for a in range(1, ssum//3+1):
        for b in range(a+1, (ssum-a)//2+1):
            c = ssum - a - b
            if a*a + b*b == c*c:
                return a*b*c


def perf(ssum):
    # use Euclid's formula for generating the triple:
    # https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
    s = ssum // 2
    limit = ceil(sqrt(s)) - 1
    for i in range(2, limit):
        if s % i == 0:
            si = s // i
            # this small trick is suggested in the problem overview
            while si % 2 == 0:
                si //= 2
            if i % 2 == 1:
                k = i + 2
            else:
                k = i + 1
            while k < 2 * i and k <= si:
                if si % k == 0 and gcd(k, i) == 1:
                    n = k - i
                    d = s // (k * i)
                    a = d * (i * i - n * n)
                    b = 2 * d * i * n
                    c = d * (i * i + n * n)
                    return a * b * c
                k += 2


if __name__ == "__main__":
    print(naive(1000))
    print(perf(1000))
    sys.exit(0)
