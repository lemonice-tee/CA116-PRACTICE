#!/usr/bin/env python3

n = int(input())
#
#if n % 3 == 0:
#    if n % 5 == 0:
#        print('fizz-buzz')
#    else:
#        print('fizz')
#elif n % 5 == 0:
#    if n % 3 == 0:
#        print('fizz-buzz')
#    else:
#        print('buzz')
#else:
#    print(n)


if n % 3 == 0 and n % 5 != 0:
    print('fizz')
elif n % 5 == 0 and n % 3 != 0:
    print('buzz')
elif n % 5 == 0 and n % 3 == 0:
    print('fizz-buzz')
else:
    print(n)
