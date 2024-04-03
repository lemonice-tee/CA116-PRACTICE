#!/usr/bin/env python3

dec = input()
bin = str()
bindiv = str()

j = 0
while j < int(dec):
    if (2 ** j) <= int(dec):
        bindiv += str(j)
    j += 1

while j != 0:
    x = int(dec)
    bin += str(x // (2 ** j))
    j -= 1

print(bin)


#if int(j) > 10:
#    print(bindiv[-2:])
#else:
print(bindiv[-1])
