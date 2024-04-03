#!/usr/bin/env python3

s = int(input())
i = 0
while i < (s / 2):
    print((' ' * (s // 2 - i)) + ('*' * (i + 1)) + (' ' * (s // 2 - i)))
    i += 1

j = i
while j > (s / 2) and j < s:
    print((' ' * (s // 2 + j)) + ('*' * (j - 1)) + (' ' * (s // 2 + j)))
    j += 1
