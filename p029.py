import sys


def main():
    seen = {}
    min_a, max_a = 2, 100
    min_b, max_b = 2, 100

    for a in range(min_a, max_a+1):
        for b in range(min_b, max_b+1):
            seen[a**b] = True
            seen[b**a] = True

    print(len(seen.keys()))


if __name__ == "__main__":
    sys.exit(main())

