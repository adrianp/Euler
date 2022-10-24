import string
import sys


def main(path):
    with open(path, "rb") as f:
        names = f.read()

    names = names.replace('"', '')
    names = names.split(",")
    names = sorted(names)

    total = 0
    for i, name in enumerate(names):
        total += (i+1) * sum([string.ascii_uppercase.index(c) + 1 for c in name])

    print(total)

    return 0


if __name__ == "__main__":
    sys.exit(main("./data/p022_names.txt"))
