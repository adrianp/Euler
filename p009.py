#The trick here is using Euclid's formula for finding the triple. Even if a 
#naive solution would work in this special case (because the numbers we search 
#for are small) using a parametrization is faster.

#Some problems one might encounter using Euclid's formula are those regarding 
#primitive triples and the fact that this formula does not generate all 
#Pythagorean triples (this can be easily fixed). You can find more info on this 
#on Wikipedia and in the problem overview

import sys
from math import ceil, sqrt 
from fractions import gcd

def main(ssum):
  s = ssum / 2
  limit = int(ceil(sqrt(s)) - 1) #casting the limit to int is needed in order 
                                 #to avoid complaints from range()
  for i in range(2,limit):
    if s % i == 0:
      si = s / i
      while si % 2==0: #this small trick is suggested in the problem overview
        si /= 2
      if i % 2 == 1:
        k = i + 2
      else:
        k = i + 1
      while k < 2 * i and k <= si:
        if si % k == 0 and gcd(k, i)==1: #note that Python has already 
                                         #implemented a GCD function
          n = k - i
          d = s / (k * i)
          a = d * (i * i - n * n)
          b = 2 * d * i * n
          c = d * (i * i + n * n)
          print a, b, c, a + b + c, a * b * c
        k += 2

if __name__ == "__main__":
  sys.exit(main(1000))
