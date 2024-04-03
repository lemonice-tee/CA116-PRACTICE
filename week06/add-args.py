#!/usr/bin/env python3

import sys

args = sys.argv[1:]
i = 0
total = 0
while i < len(args):
    n = args[i]
    total += int(n)
    i += 1

print(total)
