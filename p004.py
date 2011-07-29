import sys

#Deprecated function
def isPalyndrome(n):
  digits, i = [], 0
  while n > 0:
    c, n, i = n % 10, n/10, i+1
    digits.append(c)
  j = 0
  while j < i/2:
    if digits[j] != digits[i-j-1]:
      return False
    j += 1
  return True
  
#string version
def isPalyndrome2(n):
  string = str(n)
  return string == string[::-1]

def main():
  pal = 0
  for a in range (999, 100, -1):
    
    #Tip taken from the overview supplied after solving the problem (see last 
    #page)
    if a % 11 == 0:
      start, step = 999, 1
    else:
      start, step = 990, 11
    
    #iterating through the values of "b" using "a" as a limit makes it 
    #impossible (wrong solution given) to stop after a * b gets too small (or 
    #at least I couldn't find a way to do it)
    for b in range (start, 100, -step): 
      if a*a < pal: #because x*x > x*y where x >= y
        return pal
      if isPalyndrome2(a*b):
        if a*b > pal:
          pal = a*b
  return pal

if __name__ == "__main__":
  print main()
