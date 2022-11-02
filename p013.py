from functools import reduce
from operator import add
import sys

from data.p013_number import numbers


def main():
    print(str(reduce(add, numbers))[:10])
    return 0


if __name__ == "__main__":
    sys.exit(main())
