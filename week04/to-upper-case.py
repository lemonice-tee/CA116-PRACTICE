#!/usr/bin/env python3

i = 0
s = input()
ns = str()
capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while i < len(s):
    if s[i] not in capitals and s[i] != ' ':
        ns += s[i].capitalize()
    elif s[i] == ' ':
        ns += s[i]
    else:
        ns += s[i]
    i += 1

print(ns)
