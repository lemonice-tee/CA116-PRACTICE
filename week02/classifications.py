#!/usr/bin/env python3

n = int(input())

if n < 40:
    print('first: False')
    print('second: False')
    print('third: False')
    print('fail: True')
elif n >= 40 and n <= 49:
    print('first: False')
    print('second: False')
    print('third: True')
    print('fail: False')
elif n >= 50 and n <= 69:
    print('first: False')
    print('second: True')
    print('third: False')
    print('fail: False')
elif n >= 70:
    print('first: True')
    print('second: False')
    print('third: False')
    print('fail: False')
