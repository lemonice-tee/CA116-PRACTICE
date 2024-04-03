#!/usr/bin/env python3

s = input()
while s != 'end':
    lines = s.split()
    lines = ' '.join(lines[5:])
    print(lines)
    s = input()
