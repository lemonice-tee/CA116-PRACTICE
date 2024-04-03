#!/usr/bin/env python3

s = input()
i = 0
capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
fc = str()
while i < len(s):
    if s[i] in capitals:
        fc += s[i]
        fc += ' '
        fc += str(i)
    i += 1

if len(fc) > 0:
    print(fc)
