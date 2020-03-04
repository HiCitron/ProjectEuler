# -*- coding: utf-8 -*-
from math import sqrt

def isprem( n ):
    k = 2
    while k <= sqrt(n):
        if n%k == 0:
            return False
        k += 1
    return True

nb = 0
k = 1
r = 1
n = 1
while nb*1.0/n > 0.1 or nb == 0: 
    for i in range(4):
        k += 2*r
        if isprem( k ):
            nb += 1
    n = 1 + 4*r
    if r < 10:
        print( nb*1.0/n, nb, n )
    r += 1
print( nb*1.0/n, nb, n )