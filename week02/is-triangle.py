#!/usr/bin/env python3

n = int(input())
b = int(input())
v = int(input())
#
if n > b and n > v:
    c = n
    b = b
    a = v
elif b > n and b > v:
    c = b
    b = n
    a = v
else:
    c = v
    b = b
    a = n

#if (c ** 2) == (b ** 2) + (v ** 2):
#    print('yes')
#else:
#    print('no')

if a + b > c:
    print('yes')
else:
    print('no')
