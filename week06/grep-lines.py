#!/usr/bin/env python3

import sys
args = sys.argv[1]
s = input()
a = []
while s != 'end':
    a.append(s)
    s = input()

i = 0
while i < len(a):
    g = a[i]
    if args in g:
        print(g)
    i += 1
#i = 0
#while args in a[i]:
#    print(a[i])
#    i += 1
#i = 0
#while i < len(a):
#    l = a[i]
#    if str(args) in l:
#        print(l)
#    i += 1
#    if args in l:
#        print(l)
#    i += 1
