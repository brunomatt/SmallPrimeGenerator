# This program compiles a list of small primes.
# My Lenovo Thinkpad generates 22,044 primes in 505 seconds
import time
import math
start = time.time()

primes = [2]
odd_nums = []

def prime_check(int):
    possible_factors = []
    for k in range(2, math.ceil(int/2) + 1):
        possible_factors.append(k)
    if all(int % k for k in possible_factors) == 0:
        return False
    else:
        return True

for n in range(1, 125000): #increase/decrease upper limit for more/less primes to be generated.
    odd_nums.append(2 * n + 1)

for i in odd_nums:
    if prime_check(i) is True:
        primes.append(i)

print(primes)

stop = time.time()

print('Time: ', stop - start)