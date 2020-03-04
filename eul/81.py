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


def inv(m):
    for i in range(len(m)):
        for k in range(i):
            m[i][k],m[k][i] = m[k][i],m[i][k]
    return m


def printSM( m, n ):
    print('')
    for i in range(n):
        s = ''
        for k in range(n):
            s += str(m[i][k])+","
        print(s)

n = 80
m = inv(m)

for i in range(1, n):
    t = []
    for k in range(n):
        t.append( min([m[i-1][j] + m[i][k] + sum(m[i][k+1:j+1]) + sum(m[i][j:k]) for j in range(n)]) )
    for k in range(n):  
        m[i][k] = t[k]

print( min(m[n-1][:]) )

