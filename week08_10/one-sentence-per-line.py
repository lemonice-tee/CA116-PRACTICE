#!/usr/bin/env python3

s = input()
lines = []
i = 0
while s!= 'end':
    tokens = s.strip().split(' ')
    if len(tokens) > 0:
        lines.append(tokens)
    s = input()

i = 0
line = []
while i < len(lines):
    line += lines[i]
    i += 1
    j = 0
    p = 0
    while j < len(line):
        if line[j][p] == '.':
            ' '.join(line[:j + 1])
            p += 1
        j += 1
print(line)
#while s != 'end':
#    tokens = s.split()
#    if len(tokens) > 0:
#        lines.append(tokens)
#    s = input()

