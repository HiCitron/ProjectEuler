# -*- coding: utf-8 -*-
# Find the smallest number such that x{2,3,4,5,6} contain the same digits

#bruteforce
def ok( n ):
    b = str(n)
    for k in [2,3,4,5,6]:
        a = str(n*k)
        if len(a) > len( b ):
            return False
        else:
            t1 = []
            t2 = []
            for i in range( len(a) ):
                t1.append( a[i] )
                t2.append( b[i] )
            t1.sort()
            t2.sort()
            if t1 <> t2:
                return False
    return True
    

n = 1
while not ok( n ):
    n += 1
print(n)

# 1/7 solves that --'
# 142857