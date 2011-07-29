#The best explanation for this is in the problem overview; it took me a while
#to come up with the aproximate same solution, but some optimizations that I
#missed are explained there

import sys
from math import sqrt

#slight modification of the function used for Problems 5, 7 and 10, 
#see explanations there
def sieve(limit):
  primes = list(range(2, limit + 1))
  end = int(sqrt(limit))
  length = len(primes)
  for i in range(0, end):
    if primes[i]:
      for j in range(i + primes[i], length, primes[i]):
        primes[j] = None
  primes = filter(None, primes)
  return primes, len(primes)

def main():
  primeArray, limit = sieve(1000)
  n = 100
  #n = 10000 #possible improvement, as we search closer to the answer
  noDivsC1 = 2 #number of divisors of the "n" component
  d = 0
  while d < 500:
    n += 1
    aux = n
    noDivsC2 = 1 #number of divisors of the "n+1" component
    if aux % 2 == 0:
      aux /= 2
    for i in range(0, limit):
      if primeArray[i]*primeArray[i] > aux: #multiplication is ussualy faster 
                                            #than exponentiation
        noDivsC2 *= 2
        break
      exponent = 1
      while aux % primeArray[i] == 0:
        exponent += 1
        aux = aux/primeArray[i]
      if exponent > 1:
        noDivsC2 *= exponent
      if aux == 1:
        break
    d = noDivsC1 * noDivsC2
    noDivsC1 = noDivsC2 #the number of divisors of the "n+1" component can be 
                        #reused in the next step
  print n * (n-1) / 2 #the actual number, remember Problem 6?

if __name__ == "__main__":
  sys.exit(main())
