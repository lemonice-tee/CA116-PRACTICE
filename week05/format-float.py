#!/usr/bin/env python3

n = input()
i = 0
while i < len(n):
    if n[0] == '.':
        ff = '0' + n
    elif '.' not in n:
        ff = n + '.0'
    elif n[-1] == '.':
        ff = n + '0'
    elif n[:2] == '-.':
        ff = n[0] + '0' + n[1:]
    else:
        ff = n
    i += 1

print(ff)
