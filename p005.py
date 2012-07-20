from math import floor, log, sqrt
import sys

from euler_util import sieve


def main(nr):
    N = 1
    check = True
    limit = sqrt(nr)
    p = sieve(nr)
    a = [1] * nr
    for i in range(len(p)):
        if check:
            if p[i] <= limit:
                a[i] = floor(log(nr) / log(p[i]))
            else:
                check = False
        N *= p[i] ** a[i]
    print int(N)
    return 0

if __name__ == "__main__":
    sys.exit(main(20))
