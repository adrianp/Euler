import sys

from euler_util import fibonacci


def main():
    s, i, n = 0, 0, -1
    while n < 4000000:
        n, i = fibonacci(i), i + 1
        if n % 2 == 0:
            s += n
    print s
    return 0

if __name__ == "__main__":
    sys.exit(main())
