import sys

from euler_util import isPalyndrome


def main():
    a, largest = 999, 0

    while a >= 100:
        b, step = 999, 1
        if a % 11 != 0:
            # at least one of a or b needs to be divisible by 11; optimisation taken from overview
            # after initially solving the problem
            b, step = 990, 11

        while b >= a:
            if a*b <= largest:
                # we are going too low from now on
                break
            if isPalyndrome(a*b):
                largest = a*b
            b -= step

        a -= 1

    print(largest)


if __name__ == "__main__":
    sys.exit(main())
