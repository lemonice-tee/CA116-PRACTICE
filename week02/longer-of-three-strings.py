#!/usr/bin/env python3

fl = input()
sl = input()
tl = input()

if len(fl) > len(sl):
    if len(fl) > len(tl):
        print(fl)
    else:
        print(tl)
elif len(fl) < len(sl):
    if len(sl) > len(tl):
        print(sl)
    else:
        print(tl)
elif len(fl) < len(tl):
    if len(tl) > len(sl):
        print(tl)
    else:
        print(sl)
