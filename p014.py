# Wikipedia: Starting values with longer stopping time than any smaller
# starting value are known as "high water marks". A list of high water marks
# can be foundhere: http://oeis.org/A006877

import sys

from euler_util import hailstone


def main():
    maxc, nr, po2, pow2 = 0, -1, 1, [1]
    while True:
        po2 *= 2
        if po2 < 1000000:
            pow2.append(po2)
        else:
            break

    # this is mainly cheating (checking only odd numbers)
    # for i in range(1, 1000000, 2):
    for i in range(1000000):
        # powers of two converge to one quickly as the "increase step"
        # is never used
        if not i in pow2:
            c = hailstone(i)
            if c > maxc:
                maxc = c
                nr = i
    print nr
    return 0

if __name__ == "__main__":
    sys.exit(main())
