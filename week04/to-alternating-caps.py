#!/usr/bin/env python3

s = input()
i = 0
ns = str()
while i < len(s):
    if i % 2 == 0:
        ns += s[i].capitalize()
    else:
        ns += s[i].lower()
    i += 1

(ns)
