#!/usr/bin/env python3

import sys

with open ('test.txt') as s:
    s = sys.stdin.readlines()

i = 0
j = 0
ls = []
while i < len(s):
    j = 0
    while s[i][j] != '\n':
        ls.append(s[i][j])
        j += 1
    i += 1

c = 0
while c < len(ls):
    print(ls[c])
    c += 1
#print(ls)
