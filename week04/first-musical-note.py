#!/usr/bin/env python3

s = input()
fs = str()
mnotes = 'abcdefg'
i = 0
while i < len(s):
    if s[i] in mnotes:
        fs += s[i]
    i += 1

print(fs[0])
