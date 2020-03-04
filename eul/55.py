# -*- coding: utf-8 -*-

def isnotok( n ):
    a = n
    for i in range( 53 ):
        a = a + rev(a)
        if ispal( a ):
            return False
    return True
    
def rev( n ):
    a = str(n)
    b = ''
    for i in range( len(a) ):
        b += a[-i-1]
    return int(b)

def ispal( n ):
    if n == rev(n):
        return True
    else:
        return False


n = 0
for i in range( 10000 ):
    if isnotok( i ):
        n += 1
        print(i, n)