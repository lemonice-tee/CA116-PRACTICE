#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()
puns = 0
pune = 0
i = 0
while i < len(s):
    j = 0
    p = 0
    cs = 0
    if '(' not in s[i]:
        i += 1
    while j < len(s[i].strip()):
        if s[i][j] == ')' and j != p and cs == 0:
            pune = int(j)
            cs += 1
        j += 1
    while p < len(s[i].strip()):
        if s[i][p] == '(' and cs == 1:
            puns = int(p) + 1
            cs += 1
        p += 1
    print(s[i].strip()[puns:pune])
    i += 1
