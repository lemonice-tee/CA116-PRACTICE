#!/usr/bin/env python3

i = 0
s = input()
while i < 10:
    j = 0
    total = 0
    while j < len(s) and s[j] == '+':
        total = int(s[:j]) + int(s[j + 1:])
        j += 1
    i += 1


#i = 0
#s = input()
#while i < 10:
#    j = 0
#    total = 0
#    if s[j] == '+':
#        #print[s[j]]
#        #total = int(s[:j]) + int(s[j + 1:])
#        #print(total)
#        print(s[0])
#        j += 1
#    s = input()
#    i += 1
