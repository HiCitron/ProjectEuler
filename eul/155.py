# -*- coding: utf-8 -*-
import time

"""
sets = [[1.0],[0.5,2.0]]

t1 = time.clock()
for n in range( 2, 18 ):
    sets.append( [] )
    for j in range( int( (n+1)/2 ) ):
        # add j and n-j sets
        for i in range( len( sets[j] ) ):
            for k in range( len( sets[n-1-j] ) ):
                sets[n].append( sets[j][i] + sets[n-1-j][k] ) # serie
                sets[n].append( 1.0/ ( (1.0/sets[j][i]) + (1.0/sets[n-1-j][k]) ) ) # par
        sets[n] = list( set(sets[n]) )

    temp = []
    for i in range( len(sets) ):
        temp += sets[i]
    print( n+1, len( list(set(temp))))
print( time.clock() - t1 )


f = open( '155.txt', 'w' )
for n in range(len(sets)):
    for i in range(len(sets[n])):
        f.write( str(sets[n][i]) + "\t" )
    f.write( '\n' )
    print('Writting...'+str(n+1))
f.close()
"""

"""
def pgcd(a,b):
    if a < b:
        return(pgcd(b,a))
    else:
        r = a%b
        if r == 0:
            return(b)
        else:
            return(pgcd(b,r))
def Irred(num,den):
    div = pgcd(num,den)
    return([num/div,den/div])
def CombPara(num1,den1,num2,den2):
    numresult = num1*den2 + num2*den1
    denresult = den1*den2
    return(Irred(numresult,denresult))
def CombSerie(num1,den1,num2,den2):
    [denresult,numresult] = CombPara(den1,num1,den2,num2)
    return(Irred(numresult,denresult))
"""

"""
sets = [ [[1,1]],[[1,2],[2,1]] ]

t1 = time.clock()
for n in range( 2, 18 ):
    sets.append( [] )
    for j in range( int( (n+1)/2 ) ):
        # add j and n-j sets
        for i in range( len( sets[j] ) ):
            for k in range( len( sets[n-1-j] ) ):
                sets[n].append( [ sets[j][i][0]*sets[n-1-j][k][1] + sets[j][i][1]*sets[n-1-j][k][0], sets[j][i][1]*sets[n-1-j][k][1] ] ) # serie
                sets[n].append( [ sets[j][i][1]*sets[n-1-j][k][1] , sets[j][i][0]*sets[n-1-j][k][1] + sets[j][i][1]*sets[n-1-j][k][0] ] ) # par
    print(n)
print( time.clock() - t1 )
"""

ValC = 60
NbCMaxi = 18
def pgcd(a,b):
    if a > b :
        a,b = b,a
    r = a % b
    while r != 0:
        r = a % b
        a,b = b,r
    return(a)
def Irred(num,den):
    div = pgcd(num,den)
    return([num/div,den/div])
def CombPara(num1,den1,num2,den2):
    numresult = num1*den2 + num2*den1
    denresult = den1*den2
    return(Irred(numresult,denresult))
def CombSerie(num1,den1,num2,den2):
    [denresult,numresult] = CombPara(den1,num1,den2,num2)
    return(Irred(numresult,denresult))
def VireDoublons(TabConfig):
    TAux = list(set([str(C) for C in TabConfig]))
    TResult = []
    for T in TAux:
        s = str.split(T,",")
        num = int(s[0][1:])
        den = int(s[1][:-1])
        TResult += [[num,den]]
    return(TResult)
    
TabConfig = [[[ValC,1]]]
for NbCMax in range(1,NbCMaxi):
    TabConfig.append([])
    for NbC1 in range( int((NbCMax+1)/2) ):
        NbC2 = NbCMax - NbC1-1
        Configs1 = TabConfig[NbC1]
        Configs2 = TabConfig[NbC2]
        for C1 in Configs1:
            for C2 in Configs2:
                TabConfig[-1] += [CombPara(C1[0],C1[1],C2[0],C2[1])]
                TabConfig[-1] += [CombSerie(C1[0],C1[1],C2[0],C2[1])]
    TabConfig[-1] = VireDoublons(TabConfig[-1])
    print(NbCMax)
print("counting...")
TabAll = []
for T in TabConfig:
    TabAll += T
print("counting...")
TabAll = VireDoublons(TabAll)
print(len(TabAll))


