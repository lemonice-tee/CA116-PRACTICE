#!/usr/bin/env python3

s = input()
tt = []
while s != 'end':
    tt.append(s)
    s = input()
day = input()
i = 0
while i < len(tt):
    if tt[i][0] == day:
        print(''.join(tt[i]))
    i += 1
#print(day)
