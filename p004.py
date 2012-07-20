import sys

from euler_util import isPalyndrome


def main():
    pal = 0
    for a in range(999, 100, -1):
        # Tip taken from the overview supplied after solving the problem (see
        # last page)
        if a % 11 == 0:
            start, step = 999, 1
        else:
            start, step = 990, 11

        # iterating through the values of "b" using "a" as a limit makes it
        # impossible (wrong solution given) to stop after a * b gets too small
        # or at least I couldn't find a way to do it)
        for b in range(start, 100, -step):
            if a * a < pal:  # because x*x > x*y where x >= y
                print pal
                return 0
            if isPalyndrome(a * b):
                if a * b > pal:
                    pal = a * b
    print pal
    return 0

if __name__ == "__main__":
    sys.exit(main())
