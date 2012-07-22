import sys

from euler_util import NtoBinary

import sys
sys.setrecursionlimit(10000)

S = []
lastS = 0


def checkS(n):
    global S
    global lastS

    if len(S) > 0 and S[len(S) - 1] >= n:
        return n in S
    else:
        while True:
            lastS += 1
            ones = 0
            for i in range(lastS):
                ones += len(filter(lambda x: x == 1, NtoBinary(i)))
            S.append(ones)
            if ones == n:
                return True
            if ones > n:
                return False


def addToS(toIndex):
    global S
    global lastS
    for i in range(len(S), toIndex + 1):
        lastS += 1
        ones = 0
        for i in range(lastS):
            ones += len(filter(lambda x: x == 1, NtoBinary(i)))
        S.append(ones)


def gap(n):
    global S
    checkS(n)
    if S.index(n) + 1 >= len(S):
        addToS(S.index(n) + 1)
    return S[S.index(n) + 1] - S[S.index(n)]


def main(*args, **kwargs):
    n = kwargs["n"]
    c = kwargs["c"]
    playerOne = kwargs["playerOne"]
    start = kwargs["start"]

    if gap(c) > n and not playerOne:
        return start
    elif gap(c) > n and playerOne:
        if start == 1:
            return 0
        else:
            return main(n=n, c=0, playerOne=True, start=start - 1)
    else:
        for i in xrange(n, 0, -1):
            nextStep = c + i
            if checkS(nextStep):
                nextPlayer = not playerOne
                return main(n=n, c=nextStep, playerOne=nextPlayer, start=start)

if __name__ == "__main__":
    no = 7
    print main(n=no, c=0, start=no, playerOne=True)
