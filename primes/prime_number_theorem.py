"""
for large enough N, the number of prime numbers will be N/log(N)

first 50 000 000 prime numbers: https://primes.utm.edu/lists/small/millions/
with the largest 982 451 653

"""
import math


def pnt(N):
    return int(N/math.log(N))


N = 10**9
print("for N-numbers", N)
primes = pnt(N)
print("From PNT   there are {:d}".format(primes))
print("In reality there are {:d}".format(5*10**7))
