#!/usr/bin/env python3

n = int(input())

i = 1
while i < n + 1:
    if i % 3 == 0 and i % 5 != 0:
        print('fizz')
    elif i % 5 == 0 and i % 3 != 0:
        print('buzz')
    elif i % 15 == 0:
        print('fizz-buzz')
    else:
        print(i)
    i += 1
