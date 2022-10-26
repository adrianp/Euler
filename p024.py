import sys


def factoradic(n):
    remainders, i = [], 1

    while n > 0:
        n, r = divmod(n, i)
        remainders.append(r)
        i += 1

    return remainders[::-1]


def main():
    result = ""
    elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    f = factoradic(999999)

    for i in f:
        element = elements[i]
        result += str(elements[i])
        elements.remove(element)

    print(result)


if __name__ == "__main__":
    sys.exit(main())
