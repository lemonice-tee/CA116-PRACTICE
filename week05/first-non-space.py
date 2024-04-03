#!/usr/bin/env python3

s = input()
i = 0
fns = str()
while i < len(s) and len(fns) == 0:
    if s[i] != ' ':
        fns += str(i)
    i += 1

if len(fns) == 0:
    print('-1')
else:
    print(fns)
