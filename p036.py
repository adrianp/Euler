import sys


def main():
    found = []
    for i in range(0, 1000001):
        if str(i)[::-1] != str(i):
            continue
        b = "{0:b}".format(i)
        if str(b)[::-1] == str(b):
            found.append(i)
    print(found)
    print(sum(found))


if __name__ == "__main__":
    sys.exit(main())
