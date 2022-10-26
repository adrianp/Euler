import sys


def main():
    string = ""
    with open("./data/p008_sequence.txt", "r") as f:
        for line in f.readlines():
            string += line.strip()

    seq = 13
    digits = [int(c) for c in string]
    maximum = 0

    for i in range(len(string) - seq + 1):
        p = 1
        for j in range(seq):
            p *= digits[i + j]
        if p > maximum:
            maximum = p

    print(maximum)
    return 0


if __name__ == "__main__":
    sys.exit(main())
