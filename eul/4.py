# -*- coding: utf-8 -*-
def palin(x):
    for i in range(len(x)/2):
        if x[i] != x[-i-1]:
            return False
    return True

maxi = 0
for i in range(500,999):
    for k in range(i,999):
        if palin(str(i*k)) and i*k > maxi:
            maxi = i*k
            print(maxi)