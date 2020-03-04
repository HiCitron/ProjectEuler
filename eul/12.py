# -*- coding: utf-8 -*-
from math import sqrt

def nbdiv(x):
    n = 0
    for i in range(1,int(sqrt(x)+1)):
        if x%i == 0:
            if x/i*1.0 == i*1.0:
                n += 1
            else:
                n += 2
    return n

nb = 0
k = 0
maxi = 0
while nb < 500:
    k += 1
    nb = nbdiv(k*(k+1)*0.5)
    if nb > maxi:
        maxi = nb
        print(k,k*(k+1)*0.5,nb)