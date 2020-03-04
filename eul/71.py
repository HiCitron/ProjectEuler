# -*- coding: utf-8 -*-
from math import floor, ceil

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b) 

emin = 1
for i in range(8, 1000001):
    t = 3.0/7*i
    if gcd( floor(t), i ) == 1:
        if abs(floor( t )*1.0/i - 3.0/7) < emin:
            emin = abs(floor( t )*1.0/i - 3.0/7)
            print( floor(t), i, emin )
    if gcd(  ceil(t), i ) == 1:
        if abs( ceil( t )*1.0/i - 3.0/7) < emin:
            emin = abs( ceil( t )*1.0/i - 3.0/7)
            print( ceil(t), i, emin )