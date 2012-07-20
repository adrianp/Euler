# The trick here is using Euclid's formula for finding the triple.
# Even if a  naive solution would work in this special case
# (because the numbers we search for are small) using a parametrization is
# faster.

# Some problems one might encounter using Euclid's formula are those regarding
# primitive triples and the fact that this formula does not generate all
# Pythagorean triples (this can be easily fixed). You can find more info on
# this on Wikipedia and in the problem overview


from fractions import gcd
from math import ceil, sqrt
import sys


def main(ssum):
    s = ssum / 2
    # casting the limit to int is needed in order to avoid complaints
    # from range()
    limit = int(ceil(sqrt(s)) - 1)
    for i in range(2, limit):
        if s % i == 0:
            si = s / i
            # this small trick is suggested in the problem overview
            while si % 2 == 0:
                si /= 2
            if i % 2 == 1:
                k = i + 2
            else:
                k = i + 1
            while k < 2 * i and k <= si:
                # note that Python has already implemented a GCD function
                if si % k == 0 and gcd(k, i) == 1:
                    n = k - i
                    d = s / (k * i)
                    a = d * (i * i - n * n)
                    b = 2 * d * i * n
                    c = d * (i * i + n * n)
                    print a * b * c
                k += 2
    return 0

if __name__ == "__main__":
    sys.exit(main(1000))
