#!/usr/bin/env python3

s = input()
a = []
while s != 'end':
    a.append(s)
    s = input()

n = int(input())
i = 0
while i < len(a):
    print(a[i][0])
    i += 1
#print(n)

#print(a)
