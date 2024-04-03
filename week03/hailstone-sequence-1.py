#!/usr/bin/env python3

n = int(input())
m = int(input())

c = 0
i = 1
print(m)
while c < n + 1:
    while i < (m * n) + 1:
        if m % 2 == 0:
            x = m // 2
            print(x)
        else:
            x = (m * 3) + 1
            print(x)
        i += 1
    c += 1
