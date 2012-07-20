from operator import add
import sys

from euler_util import sieve


def main(*args, **kwargs):
    print reduce(add, sieve(2000000))
    return 0

if __name__ == "__main__":
    sys.exit(main())
