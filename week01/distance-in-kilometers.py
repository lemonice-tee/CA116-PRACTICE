#!/usr/bin/env python3

m = input()

#print(m[-3:])

if int(m[-3:]) < int(500):
    print(int(m) // 1000)
else:
    print((int(m) // 1000) + 1)
