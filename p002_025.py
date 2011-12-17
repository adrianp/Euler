#The algorithm to generate the n-th element of the Fibonacci sequence is described
#in detail on the following pages:
# [1] http://bosker.wordpress.com/2011/04/29/the-worst-algorithm-in-the-world/
# [2] http://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
# [3] http://www.ics.uci.edu/~eppstein/161/960109.html

import sys

def NtoBinary(n):
  bits = []
  while n > 0:
    n, bit = divmod(n, 2) #quotient and remainder of dividing n by 2
    bits.append(bit)
  bits.reverse()
  return bits

def fibonacci(n):
  assert n >= 0
  a, b, c = 1, 0, 1
  #Our matrix has the form:
  # a b
  # b c
  bits = NtoBinary(n)
  for bit in bits:
    if bit: 
      a, b = (a + c) * b, b * b + c * c
    else:
      a, b = a * a + b * b, (a + c) * b
    c = a + b
  return a
  
def main():
  s, i, n = 0, 0, -1
  while n < 4000000:
    n, i = fibonacci(i), i + 1
    if n % 2 == 0:
      s += n
  print s

def longfib():
  i = 0
  while len(str(fibonacci(i))) < 1000:
    i += 1
  print i-1

if __name__ == "__main__":
  sys.exit(longfib())
