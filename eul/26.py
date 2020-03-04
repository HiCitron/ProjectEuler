# -*- coding: utf-8 -*-

def dec(x):
    k = len(str(x))
    nb = [(10**k)%x]
    n = (10*nb[-1])%x
    while not(n in nb):
        nb.append(n)
        n = (10*nb[-1])%x
    return len(nb)

maxi = 0
for i in range(2,1000):
    if dec(i) > maxi:
        maxi = dec(i)
        print(maxi,i)