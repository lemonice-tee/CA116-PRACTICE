#!/usr/bin/env python3


# FOR SOME REASON WOULD ANSWER AS COMPLETELY WRONG:
#with open ('translation.txt') as f:
#    lines = f.readlines()
#
#german = {}
#i = 0
#while i < len(lines):
#    line = lines[i].rstrip().split()
#    german[line[0]] = line[1]
#    german[lines[0].rstrip(), lines[-1].rstrip()]
#    i += 1
#
#words = sys.stdin.readlines()
#c = 0
#while i < len(words):
#    trans = words[c].rstrip()
#    if trans in german:
#        print(german[trans])
#    c += 1

import sys

german = {}
i = 0
with open("translation.txt") as f:
  a = f.readlines()

while i < len(a):
    tokens = a[i].rstrip()
    list = tokens.split()
    german[list[0]] = list[1]
    i += 1
i = 0
a = sys.stdin.readlines()
while i < len(a):
    translation = a[i].rstrip()
    if translation in german:
        print(german[translation])
    i += 1
