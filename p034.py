import math
import sys

from euler_util import toDigits


def main():
    results = []
    for i in range(3, 1000000):
        if i == sum(map(math.factorial, toDigits(i))):
            results.append(i)
    print(results)
    print(sum(results))
    return 0


if __name__ == "__main__":
    sys.exit(main())
