#!/usr/bin/env python3

f = input()
i = 0
while i < len(f):
    if f[i] == '.':
        bd = f[:i]
        ad = f[i + 1:]
    i += 1

pf = str()
pf += bd + '\n' + ad
print(pf)
