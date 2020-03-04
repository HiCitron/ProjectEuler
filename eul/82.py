# -*- coding: utf-8 -*-

f = open( '82.txt')
txt = f.read()
f.close()

temp = txt.split( '\n' )
m = []
for i in range( len(temp) ):
    temp2 = temp[i].split( ',')
    m.append( [] )
    for k in range( len(temp2) ):
        m[i].append( int(temp2[k]) )


n = 80
for diag in range( 2*(n-1), -1, -1 ):
    for el in range( n - abs(diag-n+1) ):
        i = el*(diag<=n-1) + (n-1-el)*(diag>n-1)
        k = diag-i
        if i == n-1 or k == n-1:
            if k != n-1:
                # i max => droite
                m[i][k] += m[i][k+1]
            elif i != n-1:
                # k max => bas
                m[i][k] += m[i+1][k]   
        else:
            m[i][k] += min( m[i][k+1], m[i+1][k] )


            