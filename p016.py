import sys

def main():
  n, s = 2 ** 1000, 0
  while n:
    s, n = s + n % 10, n / 10
  print s

if __name__ == "__main__":
  sys.exit(main())
