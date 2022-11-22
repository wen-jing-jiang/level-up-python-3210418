import numpy

def pfactors(num):
  factors = []
  primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,83,89,97]
  for i in primes:
    if num % primes[i] == 0:
      factors.append(primes[i])

print(pfactors(1568))