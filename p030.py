from functools import reduce
from operator import add
import sys

from euler_util import toDigits


def main():
    s, total = 0, 0
    power = 5

    for current in range(10, (power+1)*9**power):
        s = reduce(add, [d**power for d in toDigits(current)])
        if s == current:
            total += current

    print(total)


if __name__ == "__main__":
    sys.exit(main())
