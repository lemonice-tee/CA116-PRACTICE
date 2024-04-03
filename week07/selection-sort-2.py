#!/usr/bin/env python3

#a = la[np:]
#i = 0
#while i < len(a):
#    p = i
#    j = i + 1
#    while j < len(a):
#        if a[j] < a[p]:
#            p = j
#        j += 1
#
#    tmp = a[p]
#    a[p] = a[i]
#    a[i] = tmp
#    i += 1
#m = 0
#while int(a[0]) != int(la[m]):
#    m += 1
#print(la)
#print(a)
#print(m)
#FROM PREV ANS
a = []
n = input()
i = 0
while n != "end":
    a.append(int(n))
    n = input()

j = int(input())
smallest = j
while j < len(a):
    if int(a[j]) < int(a[smallest]):
        smallest = j
    j = j + 1

print(smallest)
