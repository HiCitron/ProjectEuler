# -*- coding: utf-8 -*-



def find( d, p ):
    if p == 2 or p == 5:
        topop = []
        for i in range( len(d) ):
            t = str( d[i] )
            if not( t[1] in ['0','2','4','6','8'] ) and p == 2:
                topop.append( i )
            elif not t[1] in ['0','5'] and p == 5:
                topop.append( i )
        for i in range( len(topop) ):
            d.pop( topop[-i-1] )
        nd = []
        for i in range( len(d) ):
            for k in range( 10 ):
                t = str( d[i] )
                nd.append( str(k) + t)
        return nd
    else:
        c = [10%p, 100%p]
        nd = []
        for i in range( len(d) ):
            t = str( d[i] )
            r = (p - (( c[0]*int(t[0])+int(t[1]) )%p))%p
            while r%c[1] != 0:
                r += p
            r /= c[1]
            while r < 10:
                nd.append(str(r)+t)
                r += p
        return nd

d = []
for i in range( 1, int(1000/17)+1 ):
    temp = str(i*17)
    if len(temp) == 2:
        temp = '0' + temp
    d.append( temp )
temp = d[:]

prem = [13, 11, 7, 5, 3, 2]
for i in range( len(prem) ):
    d = find( d, prem[i] )
    print(' ', prem[i], d)
    topop = []
    for k in range( len(d) ):
        x = ''.join( sorted( d[k] ) )
        for l in range(1,len(x) ):
            if x[l] == x[l-1]:
                topop.append( k )
                break
    for k in range( len(topop) ):
        d.pop( topop[-k-1] )
    print(d)

s = 0
t = []
for i in range( len(d) ):
    x = ''.join( sorted( d[i] ) )
    k = 0
    while str(k) == x[k]:
        k += 1
    t.append( int( str(k)+d[i] ) )