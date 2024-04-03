#!/usr/bin/env python3

i = 0
first = 0
second = 0
third = 0
fourth = 0
fifth = 0
sixth = 0
seventh = 0
eighth = 0
ninth = 0
tenth = 0

while i < 10:
    n = int(input())
    if i == 0:
        tenth = n
    elif i == 1:
        ninth = n
    elif i == 2:
        eighth = n
    elif i == 3:
        seventh = n
    elif i == 4:
        sixth = n
    elif i == 5:
        fifth = n
    elif i == 6:
        fourth = n
    elif i == 7:
        third = n
    elif i == 8:
        second = n
    else:
        first = n
    i += 1

print(first)
print(second)
print(third)
print(fourth)
print(fifth)
print(sixth)
print(seventh)
print(eighth)
print(ninth)
print(tenth)
