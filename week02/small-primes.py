#!/usr/bin/env python3

n = int(input())
#
#primes = '23579'
#if n <= 2:
#    if n in primes or n == 11 or n == 13 or n == 17 or n == 19:
#        print('prime')
#    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 9 == 0 and n not in primes:
#        print('not prime')
#else:
#    print('prime')

if n == 2 or n == 3 or n == 5 or n == 7 or n == 11 or n == 13 or n == 17 or n == 19:
        print('prime')

else:
    print('not prime')
