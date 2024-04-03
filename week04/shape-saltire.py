#!/usr/bin/env python3

n = int(input())
i = 0
mid = n // 2
c = (n // 2) - 1
while i < n:
    if i == (n // 2):
        print((' ' * (n // 2)) + '*')
    elif i < (n // 2):
        print((' ' * i) + '*' + (' ' * ((n - 2) - (i * 2))) + '*')
    else:
        #print((' ' * i) + '*' + (' ' *
        # (1 + (i * 2))))
        #((' ' * ((n // 2) - (i % (n // 2))))
        # + '*' + (' ' * (i  % (n // 2))) + '*')
        print(((mid) - (c)) * " " + "*" + (2 * (c) - 1) * " " + "*")

    i += 1
