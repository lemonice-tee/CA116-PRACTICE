#!/usr/bin/env python3

i = 0
n = int(input())
while i < 9:
    if n < 0:
        print(str(n) + ' is negative')
    else:
        print(str(n) + ' is positive')
    n = int(input())
    i += 1
