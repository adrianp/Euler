import sys


def main():
    s = 0
    for i in range(1, 1001):
        s += i ** i
    print str(s)[-10:]
    return 0

if __name__ == "__main__":
    sys.exit(main())
