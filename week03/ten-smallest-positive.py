#!/usr/bin/env python3

i = 0
smallest = 500
while i < 10:
    n = int(input())
    if n > 0 and n < smallest:
        smallest = n
    i += 1

print(smallest)
