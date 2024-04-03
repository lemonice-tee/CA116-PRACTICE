#!/usr/bin/env python3

s = input()
i = 0
fs = str()
digits = '1234567890'
while i < len(s) and len(fs) == 0:
    if s[i] in digits:
        fs += s[i]
        fs += ' '
        fs += str(i)
    i += 1

if len(fs) > 0:
    print(fs)
