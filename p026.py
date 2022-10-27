import sys


def cycle_size(n, d):
    result, seen = "", {}
    remainder = n % d
    while remainder != 0 and remainder not in seen:
        seen[remainder] = len(result)
        remainder *= 10
        r, remainder = divmod(remainder, d)
        result += str(r)
    if remainder == 0:
        return 0
    return len(result[seen[remainder]:])


def main():
    max_len, nr = 0, 0
    for i in range(2, 1001):
        cycle = cycle_size(1, i)
        if cycle > max_len:
            max_len, nr = cycle, i
    print(nr)


if __name__ == "__main__":
    cycle_size(1, 7)
    sys.exit(main())
