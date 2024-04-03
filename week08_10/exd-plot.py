#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

i = 0
ls = []
while i < len(s):
    ls.append(int(s[i].rstrip()))
    i += 1
#selection sort to organise numbers
#i = 0
#while i < len(ls):
#   p = i
#   j = i + 1
#   while j < len(ls):
#       if ls[j] < ls[p]:
#           p = j
#       j += 1
#   tmp = ls[p]
#   ls[p] = ls[i]
#   ls[i] = tmp


i = 0
pos = []
while i < ls[0]:
    if i in ls:
        pos.append(i + 1)
    i +=1
#print(pos)

#i = 0
#while i < ls[0]:
plot = []
j = 0
while j < int(pos[-1] + 2):
    if j == int(0):
        plot.append('|')
    elif j != int(0) and j in pos and j < int(pos[-1] + 1):
        plot.append('*')
    elif j != int(0) and j not in pos and j < int(pos[-1] + 1):
        plot.append(' ')
    else:
        plot.append('|')
    j += 1
#i += 1
#print(line)

print(''.join(plot))
