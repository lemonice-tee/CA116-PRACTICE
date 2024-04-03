#!/usr/bin/env python3

even = []
odd = []
s = input()
while s != 'end':
    if int(s) % 2 == 0:
        even.append(s)
    else:
        odd.append(s)
    s = input()

e = 0
while e < len(even):
    print(even[e])
    e += 1
o = 0
while o < len(odd):
    print(odd[o])
    o += 1
#print(even)
#print(odd)
