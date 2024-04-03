#!/usr/bin/env python3

i = 0
largest = 20
while i < 10:
    n = int(input())
    if n > largest:
        largest = n
    i += 1

print(largest)
