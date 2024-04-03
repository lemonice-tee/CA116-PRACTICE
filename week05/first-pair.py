#!/usr/bin/env python3

s = input()
i = 1
while i < len(s):
    if s[i] == s[i - 1]:
        print(s[i:i - 1])
    else:
        i += 1
    i += 1

