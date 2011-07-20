import sys
from math import factorial

def main():
  n, s = factorial(100), 0
  while n:
    s, n = s+n%10, n/10
  print s

if __name__ == "__main__":
  sys.exit(main())
