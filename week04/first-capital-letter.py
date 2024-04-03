#!/usr/bin/env python3

i = 0
s = input()
capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
fc = str()
while i < len(s) and len(fc) == 0:
    if s[i] in capitals:
        fc += str(i)
    i += 1

print(int(fc))
