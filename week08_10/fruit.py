#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

fruit = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}

i = 0
while i < len(lines):
    if lines[i].rstrip() in fruit:
        print(lines[i].rstrip())
    i += 1
#print(lines)
