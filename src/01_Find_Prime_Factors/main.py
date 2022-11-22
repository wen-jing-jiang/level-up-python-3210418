def pfactors(num):
    factors = []
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,83,89,97]
    for i in primes:
        while num % i == 0:
            factors.append(i)
            num = num/i
    if len(factors) == 0:
        factors.append(num)
    else:
        print(factors)


pfactors(77)