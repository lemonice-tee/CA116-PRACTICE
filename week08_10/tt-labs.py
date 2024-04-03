#!/usr/bin/env python3

s = input()
days = []
while s != 'end':
    lines = s.split()
    days.append(lines)
    s = input()
i = 0
while i < len(days):
    hr = days[i][2]
    if int(hr) > 1:
        print(' '.join(days[i]))
    i += 1
