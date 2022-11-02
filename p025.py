import sys

from euler_util import fibonacci


def main():
    i = 0
    while len(str(fibonacci(i))) < 1000:
        i += 1
    print(i - 1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
