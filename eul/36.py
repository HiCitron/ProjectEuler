# -*- coding: utf-8 -*-



def Bin(n):
    return int( bin(n)[2:])


def IsPal(n):
    n = str(n)
    for i in range( int(len(n)/2) ):
        if n[i] != n[-i-1]:
            return False
    return True

s = 0
for k in range( 1000000 ):
    if IsPal(k):
        if IsPal ( Bin(k) ):
            s += k
            print( k, Bin(k), s)