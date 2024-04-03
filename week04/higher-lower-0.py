#!/usr/bin/env python3
#
#prev = int(input())
#curr = int(input())
#while prev != 0 and curr != 0:
#    if prev < curr:
#        print('higher')
#    elif prev > curr:
#        print('lower')
#    else:
#        print('equal')
#    prev = curr
#    curr = int(input())


prev = int(input())
while prev != 0:
    curr = int(input())
    while curr != 0:
        if prev < curr:
            print('higher')
        elif prev > curr:
            print('lower')
        elif curr == prev:
            print('equal')
#        else:
#
        prev = curr
        curr = int(input())
