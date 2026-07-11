# Author: Munna
# Date: 12/07/2026

'''
Write a function called next_prime, which returns a generator that will yield an unlimited 
number of primes, starting from the first prime (2).

Recall that a prime number is any whole number that has exactly two divisors: one and the 
number itself. The first few primes are 2, 3, 5, 7, 11, ... .

For example:
primes = next_prime()
[next(primes) for i in range(25)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

algorithm:
1. Define a function called next_prime that returns a generator:
   a. Initialize an empty list to store the primes
   b. Start with the first prime (2)
   c. For each subsequent number, check if it's prime
      i. If it is, yield it and add it to the list
      ii. If not, continue to the next number
'''

def next_prime():
    primes = []
    num = 2
    while True:
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num
        num += 1
primes = next_prime()
print([next(primes) for i in range(25)])