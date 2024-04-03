#!/usr/bin/env python3

n = int(input())
i = 0
j = i + 1
fib = []
fib.append(i)
fib.append(j)
while n > 0 and i != n:
    k = i + j
    fib.append(k)
    j = k
    i = j

if n in fib:
    print('yes')
else:
    print('no')

print(fib)
# fibonacci = i + j, where j = i + 1 == k; i = j and j = k
#print(n)
