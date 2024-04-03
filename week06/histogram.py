#!/usr/bin/env python3

s = input()
i = 0
l0 = []
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
l8 = []
l9 = []

while s != 'end':
    if s == '0':
        l0.append('*')
    if s == '1':
        l1.append('*')
    if s == '2':
        l2.append('*')
    if s == '3':
        l3.append('*')
    if s == '4':
        l4.append('*')
    if s == '5':
        l5.append('*')
    if s == '6':
        l6.append('*')
    if s == '7':
        l7.append('*')
    if s == '8':
        l8.append('*')
    if s == '9':
        l9.append('*')
    s = input()

print('0', (len(l0) * '*'))
print('1', (len(l1) * '*'))
print('2', (len(l2) * '*'))
print('3', (len(l3) * '*'))
print('4', (len(l4) * '*'))
print('5', (len(l5) * '*'))
print('6', (len(l6) * '*'))
print('7', (len(l7) * '*'))
print('8', (len(l8) * '*'))
print('9', (len(l9) * '*'))
