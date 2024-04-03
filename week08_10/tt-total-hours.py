#!/usr/bin/env python3

s = input()
hr = []
while s != 'end':
    lines = s.split()
    hr.append(lines[2])
    s = input()
i = 0
total = 0
while i < len(hr):
    h = hr[i]
    total += int(h)
    i += 1
print(total)
