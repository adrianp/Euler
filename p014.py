#Wikipedia: Starting values with longer stopping time than any smaller starting 
#value are known as "high water marks". A list of high water marks can be found 
#here: http://oeis.org/A006877

#I think this problem is a good candidate for a Genetic Algorithm

import sys

def hailstone(n):
  c = 0 #I don't count the starting number
  while n > 1:
    if n % 2 == 1:
      n = (3 * n + 1) / 2 #this is a visible improvement (The Collatz 
                          #conjecture is defined as a parity sequence)
    else:
      n /= 2
    c += 1
  return c

def main():
  maxc, nr, po2, pow2 = 0, -1, 1, [1]
  while True:
    po2 *= 2
    if po2 < 1000000:
      pow2.append(po2)
    else:
      break
  #for i in range(1,1000000,2): #this is mainly cheating (checking only odd 
                                #numbers)
  for i in range(1000000):
    if not i in pow2: #powers of two converge to one quickly as the "increase 
                       #step" is never used
      c = hailstone(i)
      if c > maxc:
        maxc = c
        nr = i
  print nr

if __name__ == "__main__":
  sys.exit(main())
