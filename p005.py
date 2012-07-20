#At first I resolved problem 5 on paper, as it is quite simple to do that
#But on the Euler website there is suggested a solution  that can be 
#implemented. The catch is that we need the first N-th prime numbers.
#For that, I implemented the Sieve of Eratosthenes: 
#http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#And since we have that sieve, we can use it also for other problems, like 7 or
#10; it is also used in other scripts in the project

import sys
from math import sqrt, floor, log
from operator import add

def sieve(limit):
  primes = list(range(2, limit+1))
  end = int(sqrt(limit)) #this trick is explained on Wikipedia
  length = len(primes)
  for i in range(0, end):
    if primes[i]:
      for j in range(i + primes[i], length, primes[i]): #you need to be very 
                                                      #careful with this loop
        primes[j] = None
  return filter(None, primes)

def snd(nr):
  N = 1
  check = True
  limit = sqrt(nr)
  p = sieve(nr)
  a = [1] * nr
  for i in range(len(p)):
    if check:
      if p[i] <= limit:
        a[i] = floor(log(nr) / log(p[i]))
      else:
        check = False
    N *= p[i] ** a[i] #if you are not familiar with Python, ** 
                      #is the exponentation operation
  return N

if __name__ == "__main__":
  print snd(20) #Problem 5
  #Since we know the answer now, we could choose the sieve limit somewhere closer to
  #the 10001st prime (104743)
  print sieve(200000)[10000] #Problem 7, notice 10001
  print reduce(add, sieve(2000000)) #Problem 10
  
