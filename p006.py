import sys


def naive(n):
    sumSquares, ssum = 0, 0
    for i in range(n + 1):
        sumSquares += i * i
    # notice the mistake in the description
    print n * n * (n + 1) * (n + 1) / 4 - sumSquares
    return 0


def fast(n):
    # while the sum of the first n numbers has a well-known formula, I
    # didn't figure out one for the sum of squares (see problem overview)
    print n * n * (n + 1) * (n + 1) / 4 - (2 * n + 1) * (n + 1) * n / 6
    return 0

if __name__ == "__main__":
    sys.exit(fast(100))
