#!/usr/bin/env python3

s = input()
i = 0
a = []
while s != 'end':
    a.append(s)
    s = input()

a = a[::-1]
while i < len(a):
    print([i])
    i += 1
