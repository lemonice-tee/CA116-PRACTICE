#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
trans = {
    'one': 'eins',
    'two': 'zwei',
    'three': 'drei',
    'four': 'vier',
    'five': 'funf',
    'six': 'sechs',
    'seven': 'sieben',
    'eight': 'acht',
    'nine': 'neun',
    'ten': 'zehn',
}

i = 0
while i < len(lines):
    if lines[i].rstrip() in trans:
        print(trans[lines[i].rstrip()])
    i += 1
