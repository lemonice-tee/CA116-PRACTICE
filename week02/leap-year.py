#!/usr/bin/env python3

y = int(input())

#if y % 4 == 0 or y % 400 == 0 and :
#    print('True')
#else:
#    print('False')

if y % 100 == 0:
    if y % 400 == 0 or y % 4 == 0:
        print('True')
    else:
        print('False')
else:
    print('False')
