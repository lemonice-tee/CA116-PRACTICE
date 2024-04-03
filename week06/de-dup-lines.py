#!/usr/bin/env python3

s = input()
seen = []
i = 0
while s != 'end':
    if s not in seen:
        seen.append(s)
    s = input()

while i < len(seen):
    print(seen[i])
    i += 1

#print(seen)
#s = input()
#i = 0
#a = []
#while s != 'end':
#    if s not in a:
#        a.append(s)
#    s = input()
##IS CORRECT
#i = 0
#while i < len(a):
#    print(a[i])
#    i += 1
