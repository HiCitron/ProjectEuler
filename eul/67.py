# -*- coding: utf-8 -*-

f = open( '67.txt' )
txt = f.read()

nbp = 16

t = txt.split('\n')
for i in range( len(t) ):
    t[i] = t[i].split(' ')
t.pop()
for i in range(nbp):
    t.append([])
    for k in range( len(t) ):
        t[-1].append( 0 )


def gench( n ):
    ch = [[]]
    for i in range(n):
        nch = []
        for k in range(len(ch)):
            temp1 = ch[k][:]
            temp2 = ch[k][:]
            temp1.append(0)
            temp2.append(1)
            nch.append( temp1 )
            nch.append( temp2 )
        ch = nch[:][:]
    return ch
        

def bestprev( t, chemin, nbp, allw ):
    e = len(chemin)-1
    m = 0
    choix = 0
    for i in range( len( allw) ):
        s = 0
        temp = chemin[:]
        for k in range( nbp ):
            s += int( t[ e + k + 1 ][ temp[-1] + allw[i][k] ] )
            temp.append( temp[-1]+allw[i][k] )
        if s > m:
            m = s
            choix = temp[-nbp]
            #print( allw[i], m, temp )
    return choix

allw = gench( nbp )
chemin = [0]
s = 0
for e in range( 100 ):
    s += int( t[e][chemin[-1]] )
    chemin.append( bestprev( t, chemin, nbp, allw) )
    print(e)
print(s)