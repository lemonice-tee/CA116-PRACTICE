#!/usr/bin/env python3

i = 0
total = 0
while i < 10:
    n = int(input())
    if n < 0:
        total += (n * -1) % 10
    else:
        total += (n % 10)
    i += 1

print(total)
