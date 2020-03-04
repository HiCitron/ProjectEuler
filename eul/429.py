# -*- coding: utf-8 -*-
from math import sqrt
from fractions import gcd

def udiv(x):
    r = []
    for i in range(1,int(sqrt(x)+1)):   
        if x%i == 0 and gcd(i,x/i) == 1:
            r.append(i)
            r.append(x/i)
    return r

n = []
for k in range(10000):
    print(k)
    for i in range(10000):
        a = k*10000 + i
        t = udiv(a)
        for l in range(len(t)):
            if not(t[l] in n):
                n.append(t[l])
    n.sort()
