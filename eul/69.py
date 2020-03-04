# -*- coding: utf-8 -*-
from math import sqrt

def iniprem(n):
    array = [2]
    for i in range(3,n):
        prem = True
        k = 0
        while array[k] <= int(sqrt(i)):
            if i%array[k] == 0:
                prem = False
                break
            k += 1
        if prem:
            array.append(i)
    return array



def divprem(n):
    if n in array:
        return [n]
    else:
        prem = []
        k = 0
        while array[k] <= n:
            if n%array[k] == 0:
                n = n/array[k]
                if not(array[k] in prem):
                    prem.append(array[k])
            else:
                k += 1
        return prem

def areprem(x,y):
    p1 = divprem(x)
    p2 = divprem(y)
    for i in range(len(p1)):
        if p1[i] in p2:
            return False
    return True

def phi(n):
    nb = 0
    for i in range(1,n):
        if areprem(n,i):
            nb += 1
    return nb

print('Starting...')
global array
array = iniprem(1000000)
print('1/2')
a = []
for i in range(2,1000000):
    a.append(divprem(i))
    if i%100 == 0:
        print(i*1.0)
print('Init done')