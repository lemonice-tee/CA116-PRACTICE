#!/usr/bin/env python3

n = int(input())
total = 0
while n != 0:
    if n < 0:
        total += (n * -1)
    else:
        total += n
    n = int(input())

print(total)
