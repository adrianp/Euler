import logging
import sys

from euler_util import sieve

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def rotate(s):
    return s[-1] + s[:-1]


def main():
    limit = 1000000
    primes = sieve(limit)
    found = []
    for i in primes:
        logging.info(f"At {i}")
        all_primes = True
        rot = str(i)
        if i > 9 and (any([c in "024568" for c in rot])):
            continue
        while True:
            rot = rotate(rot)
            if rot[0] == "0":
                continue
            if int(rot) == i:
                break
            if int(rot) not in primes:
                all_primes = False
                break
        if all_primes:
            found.append(i)
    print(len(found))
    return 0


if __name__ == "__main__":
    sys.exit(main())
