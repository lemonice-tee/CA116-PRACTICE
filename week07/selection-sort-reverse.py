#!/usr/bin/env python3

a = []
s = input()
i = 0
while s != 'end':
    a.append(s)
    s = input()

while i < len(a):
    p = i
    j = i + 1
    while j < len(a):
        if int(a[j]) < int(a[p]):
            p = j
        j += 1

    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp

    i += 1

m = 0
a = a[::-1]
while m < len(a):
    print(a[m])
    m += 1
#m = 1
#while m < len(a) + 1:
#    print(a[-1 * m])
#    m += 1
#print(a[::-1])
