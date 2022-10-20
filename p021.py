import sys

from euler_util import divisors


def naive(limit):
    sums = {}
    for i in range(1, limit):
        sums[i] = sum(divisors(i))

    total = 0
    for nr, d in sums.items():
        if d in sums and sums[d] == nr and nr != d:
            total += nr
    print(total)


if __name__ == "__main__":
    sys.exit(naive(10000))
