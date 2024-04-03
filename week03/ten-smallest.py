#!/usr/bin/env python3

i = 0
smallest = 5
while i < 10:
    n = int(input())
    if n < smallest:
        smallest = n
    i += 1

print(smallest)
