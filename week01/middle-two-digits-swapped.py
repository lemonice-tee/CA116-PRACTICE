#!/usr/bin/env python3

n = int(input())

n = (n // 100) % 100
r = str(n)
print(r[::-1])
