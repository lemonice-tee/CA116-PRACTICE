#!/usr/bin/env python3

fn = int(input())
sn = int(input())
tn = int(input())

if fn == sn and fn == tn:
    print('True')
elif fn == sn and fn != tn:
    print('True')
elif fn != sn and fn == tn:
    print('True')
elif sn == tn and fn != tn:
    print('True')
else:
    print('False')
