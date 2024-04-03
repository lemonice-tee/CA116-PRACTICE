#!/usr/bin/env python3

s = input()
a = []
i = 0
while s != 'end':
    a.append(int(s))
    s = input()
while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j += 1
    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp
    i += 1

#print(a)
print(int(a[len(a) // 2]))
