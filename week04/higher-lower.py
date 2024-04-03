#!/usr/bin/env python3

prev = int(input())
i = 0
while i < 5:
    curr = int(input())
    if curr < prev:
        print('lower')
    elif curr > prev:
        print('higher')
    else:
        print('equal')
    prev = curr
    i += 1
