#!/usr/bin/env python3

s = input()
while s != 'end':
    lines = s.split()
    if lines[0] == '3':
        print(' '.join(lines))
    s = input()
#    lines = s.split()
#    if lines[0] == 3:
#        print(''.join(lines))
#    s = input()
