#!/usr/bin/env python3

s = input()
i = 0
digits = '1234567890'
fn = str()
#j = 0
while i < len(s):
    if s[i] in digits:
        j = int(i) + 1
        if s[j] not in digits:
            print(s[i:j])
        j += 1
    i += 1
#fn += s[i:j]
#print(fn)
print(i)
