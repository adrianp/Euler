import sys

#this is the naive method
def naive(n):
  sumSquares, ssum = 0, 0
  for i in range (n+1): #seems that the first 100 natural numbers are 1..100
    sumSquares += i*i
  print n*n*(n+1)*(n+1)/4 - sumSquares #notice the mistake in the description
  
def fast(n):
  #while the sum of the first n numbers has a well-known formula, I didn't figure
  #one for the sum of squares (see problem overview)
  print n*n*(n+1)*(n+1)/4 - (2*n+1)*(n+1)*n/6 #maybe this can be simplified?

if __name__ == "__main__":
  fast(100)
