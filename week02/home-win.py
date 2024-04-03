#!/usr/bin/env python3

ht = int(input())
at = int(input())

if ht > at:
    print('Home win.')
elif ht < at:
    print('Away win.')
else:
    print('Draw.')
