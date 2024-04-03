#!/usr/bin/env python3

s = input()
i = 0
a = []
while s != 'end':
    a.append(int(s))
    s = input()
m = []
if s == 'end':
    s = input()
    m = int(s)

i = 0
while i < len(a):
    n = a[i]
    print(int(n) + m)
    i += 1
#print(m)
#print(a)
