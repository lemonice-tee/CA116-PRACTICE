#!/usr/bin/env python3

m = int(input())
d = int(input())

x = ((((m - 1) * 30) + d) % 7)

if x == 0:
  print(7)
else:
  print(x)
