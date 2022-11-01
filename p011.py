import sys

from data.p011_grid import matrix


def main():
    seq, maxp = 4, 0
    for i in range(len(matrix) - seq):
        for j in range(len(matrix[0]) - seq):
            # down; we don't need to check in the "up" direction also,
            # as we would check the same numbers twice
            prod = 1
            for k in range(seq-1):
                prod *= matrix[i + k][j]
            if prod > maxp:
                maxp = prod

            # right
            prod = 1
            for k in range(seq-1):
                prod *= matrix[i][j + k]
            if prod > maxp:
                maxp = prod

            # main diagonal
            prod = 1
            for k in range(seq-1):
                prod *= matrix[i + k][j + k]
            if prod > maxp:
                maxp = prod

            # antidiagonal
            # notice that we need to check this also, even if there is no
            # clue about it in the problem description
            if j > seq - 2:
                prod = 1
                for k in range(seq):
                    prod *= matrix[i + k][j - k]
                if prod > maxp:
                    maxp = prod
    print(maxp)
    return 0


if __name__ == "__main__":
    sys.exit(main())
