# -*- coding: utf-8 -*-

# But: nb ^ 3 = n
# Permutations sur n
# trouve 5 perm tq ils sont des ^3

def sort(n):
    t = []
    for i in range( len(str(n))-1, -1, -1 ):
        temp = int(n / 10**i)
        n = n-temp*10**i
        t.append( temp )
    t.sort()
    t = t[::-1]
    n = ''
    for i in range( len(t) ):
        n += str(t[i])
    return int(n)



for nbd in range( 8, 25 ):
    maxi = int((10**(nbd)-1)**0.333333)+1
    mini= int((10**(nbd-1))**0.333333)+1
    
    t = { }
    for i in range(mini,maxi):
        if sort(i**3) not in t:
            t[sort(i**3)] = [i]
        else:
            t[sort(i**3)].append( i )
    
    for i in t:
        if len(t[i]) == 5:
            print( t[i] )