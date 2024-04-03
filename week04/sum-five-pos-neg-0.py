#!/usr/bin/env python3

n = int(input())
total_pos = 0
total_neg = 0

while n != 0:
    if n < 0:
        total_neg += n
    else:
        total_pos += n
    n = int(input())

print(total_neg, total_pos)
