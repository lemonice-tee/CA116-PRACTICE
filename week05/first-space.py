#!/usr/bin/env python3

i = 0
s = input()
fs = str()
while i < len(s) and len(fs) == 0:
    if s[i] == ' ':
        fs += str(i)
    i += 1

if len(fs) == 0:
    print('-1')
else:
    print(fs)
