#!/usr/bin/env python3

n = int(input())

i = 1
while i < (n * 7) + 1:
    if i % 7 == 0:
        print(i)
    i += 1
