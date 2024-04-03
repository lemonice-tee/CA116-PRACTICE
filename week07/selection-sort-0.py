#!/usr/bin/env python3

#ANS. W/ SELECTION SORT

s = input()
a = []
while s != 'end':
    a.append(int(s))
    s = input()

i = 0
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

print(a[0])

#smallest = input()
#s = input()
#i = 0
#while s != 'end':
#    if int(s) < int(smallest):
#        smallest = int(s)
#    s = input()
#
#print(smallest)
