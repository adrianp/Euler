import sys

from euler_util import sieve


def main(*args, **kwargs):
    # Since we know the answer now, we could choose the sieve limit somewhere
    # closer to the 10001st prime (104743)
    print sieve(200000)[10000]
    return 0  # notice 10001


if __name__ == "__main__":
    sys.exit(main())
