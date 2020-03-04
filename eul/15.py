# -*- coding: utf-8 -*-

def fact(x):
    p = 1
    for i in range(1,x+1):
        p *= i
    return p

def C(k,n):
    return fact(n)/(fact(k)*fact(n-k))

print(C(20,40))