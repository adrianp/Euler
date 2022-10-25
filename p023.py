import sys

from euler_util import divisors


def main():
    limit = 28125

    abundant_numbers = []
    for i in range(0, limit):
        if sum(divisors(i)) > i:
            abundant_numbers.append(i)

    numbers = {}
    for i, vi in enumerate(abundant_numbers):
        for j, vj in enumerate(abundant_numbers):
            numbers[vi+vj] = True

    total = 0
    for i in range(0, limit):
        if i not in numbers:
            total += i

    print(total)

    return 0


if __name__ == "__main__":
    sys.exit(main())
