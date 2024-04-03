#!/usr/bin/env python3

n = int(input())
m = int(input())

i = 1
while i < (n * m) + 1:
    if i % m == 0:
        print(i)
    i += 1
