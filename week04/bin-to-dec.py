#!/usr/bin/env python3

i = 0
bin = input()
dec = 0
while i < len(bin):
    #dec += int((bin[len(bin) - i]) * (2 ** (i))
    dec += int(bin[i]) * (2 ** (len(bin) - i - 1))
    i += 1

print(dec)
