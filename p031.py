import sys


def generate_superset(target):
    i = 0
    current = [0] * target
    current[i] = target
    partitions = []

    while True:
        # slicing until i+1 ensures we don't go over the target
        partition = current[0:i+1]
        partitions.append(partition)

        remaining = 0

        # count how many 1s we have in the current partition
        while i >= 0 and current[i] == 1:
            remaining += current[i]
            i -= 1

        # all elements in partition are 1, this is the last element
        if i < 0:
            return partitions

        # to move to the next partition we need to subtract 1 from the
        # rightmost elements which is not 1...
        current[i] -= 1
        # ... and add that 1 to the remainder
        remaining += 1

        # we now spread the remainder over the remaining elements
        while remaining > current[i]:
            current[i+1] = current[i]
            remaining -= current[i]
            i += 1

        current[i+1] = remaining
        i += 1

    return partitions


def change(total, coins):
    if total == 0:
        return 1
    if not coins or total < 0:
        return 0
    return change(total - coins[0], coins) + change(total, coins[1:])


def main(target=5):
    print(change(200, [1, 2, 5, 10, 20, 50, 100, 200]))
    return 0


if __name__ == "__main__":
    sys.exit(main(200))
