# -*- coding: utf-8 -*-

def P( t, n ):
    if t == 3:
        return n*(n+1)/2
    elif t == 4:
        return n**2
    elif t == 5:
        return n*(3*n-1)/2
    elif t == 6:
        return n*(2*n-1)
    elif t == 7:
        return n*(5*n-3)/2
    elif t == 8:
        return n*(3*n-2)

def getPairs( t ):
    i = 0
    while P( t, i) < 10**3:
        i += 1
    tab = []
    for k in range( 10, 100):
        tab.append([])
        while int(str(P(t,i))[0:2]) == k:
            tab[k-10].append(P(t,i))
            i += 1
    return tab

def nextPoss( n, t, gP):
    if int(str(n)[-2:]) < 10:
        return False
    else:
        tab = []
        n = int(str(n)[-2:])
        for k in [x for x in range(3,9) if x not in t]:
            tab.append( [k, gP[k-3][n-10] ])
        return tab

gP = []
for k in range(3,9):
    gP.append( getPairs(k) )

for k in range(10,100):
    for i in range( len(gP[0][k-10]) ):
        t = [3]
        nP1 = nextPoss( gP[0][k-10][i], t, gP )
        if nP1:
            for t1 in range( len(nP1) ):
                for n1 in range( len(nP1[t1][1]) ):
                    t = [3, nP1[t1][0] ]
                    nP2 = nextPoss( nP1[t1][1][n1], t, gP )
                    if nP2:
                        for t2 in range( len(nP2) ):
                            for n2 in range( len(nP2[t2][1]) ):
                                t = [3, nP1[t1][0], nP2[t2][0] ]
                                nP3 = nextPoss( nP2[t2][1][n2], t, gP )
                                if nP3:
                                    for t3 in range( len(nP3) ):
                                        for n3 in range( len(nP3[t3][1]) ):
                                            t = [3, nP1[t1][0], nP2[t2][0], nP3[t3][0] ]
                                            nP4 = nextPoss( nP3[t3][1][n3], t, gP )
                                            if nP4:
                                                for t4 in range( len(nP4) ):
                                                    for n4 in range( len(nP4[t4][1]) ):
                                                        t = [3, nP1[t1][0], nP2[t2][0], nP3[t3][0], nP4[t4][0] ]
                                                        nP5 = nextPoss( nP4[t4][1][n4], t, gP )
                                                        if nP5:
                                                            for t5 in range( len(nP5) ):
                                                                for n5 in range( len(nP5[t5][1]) ):
                                                                    t = [3, nP1[t1][0], nP2[t2][0], nP3[t3][0], nP4[t4][0], nP5[t5][0] ]
                                                                    if int(str(nP5[0][1][n5])[-2:]) == int(str(gP[0][k-10][i])[0:2]):
                                                                        print( gP[0][k-10][i], nP1[t1][1][n1], nP2[t2][1][n2], nP3[t3][1][n3], nP4[t4][1][n4], nP5[0][1][n5])
                                                                        print(t)

