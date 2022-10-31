import sys


def print_matrix(matrix):
    zfill = len(str(len(matrix) * len(matrix[0])))
    for line in matrix:
        print(" ".join([str(x).zfill(zfill) for x in line]))


def main():
    size = 1001
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    i, j = 0, size - 1
    current_bound = [1, size-1]
    current = size * size
    passed = 0

    while current > 1:
        if passed % 2 == 1:
            while j < current_bound[1]:
                matrix[i][j] = current
                current -= 1
                j += 1
            while i >= current_bound[0]:
                matrix[i][j] = current
                current -= 1
                i -= 1
            current_bound[1] -= 1
        else:
            while j >= current_bound[0]:
                matrix[i][j] = current
                current -= 1
                j -= 1
            while i < current_bound[1]:
                matrix[i][j] = current
                current -= 1
                i += 1
            current_bound[0] += 1
        passed += 1
    matrix[size//2][size//2] = 1

    result = 0

    i = 0
    while i < size:
        element1 = matrix[i][i]
        element2 = matrix[i][size-i-1]
        result += element1 + element2
        i += 1

    print(result-1)


if __name__ == "__main__":
    sys.exit(main())
