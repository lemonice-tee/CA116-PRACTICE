#!/usr/bin/env python3

s = input()
rms = str()
i = 0
while i < len(s):
    if s[i] != ' ':
        rms += s[i]
    i += 1

print(rms)
