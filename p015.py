# You can find a good explanation of this solution here:
# http://joaoff.com/2008/01/20/a-square-grid-path-problem/
# The keypoint is that we need to go down the same number of times we go right

import sys

from euler_util import binomial


def main(*args, **kwargs):
    print(binomial(2 * args[0], args[0]))
    return 0


if __name__ == "__main__":
    sys.exit(main(20))
