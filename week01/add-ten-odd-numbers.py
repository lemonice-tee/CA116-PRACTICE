#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
j = int(input())

total = 0

while a % 2 != 0:
    total += a
    if b % 2 != 0:
        total += b
    elif c % 2 != 0:
        total += c
    elif d % 2 != 0:
        total += d
    elif e % 2 != 0:
        total += e
    elif f % 2 != 0:
        total += f
    elif g % 2 != 0:
        total += g
    elif h % 2 != 0:
        total += h
    elif i % 2 != 0:
        total += i
    elif j % 2 != 0:
        total += j

    print(total)

#if n % 2 == 0:
#    total = total + n
#    m = int(input())
#else:
#    m = int(input())
