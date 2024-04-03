#!/usr/bin/env python3

a = int(input())
b = int(input())
i = 1
gcd = str()
while i < a: #and b != 0 and a != 0:
    if i % a == 0 and i % b == 0:
        gcd += str(i) + ' '
    i += 1
print(gcd)
