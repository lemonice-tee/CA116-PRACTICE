#!/usr/bin/env python3

#ANS. W/ SELECTION SORT

s = input()
a = []
while s != 'end':
    a.append(int(s))
    s = input()
i = 0
j = i + 1
while j < len(a):
    if a[j] < a[i]:
        i = j
    j += 1

print(i)

#ATTEMPT NO. 1
#while i < len(a):
#    j = i + 1
#    while j < len(a):
#        if a[j] < a[i]:
#            p = j
#        j += 1
#    i += 1
#print(p)

#sp = 0
#smallest = int(input())
#i = 0
#s = input()
#while s != 'end':
#    if int(s) < smallest:
#        smallest = int(s)
#        sp = i + 1
#    i += 1
#    s = input()
#
#print(sp)
