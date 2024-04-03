#!/usr/bin/env python3

s = input()
i = 0
j = 0
a = []
while s != 'end':
    a.append(s)
    s = input()

while i < len(a):
    print(i, len(a), a[i])
    i += 1
