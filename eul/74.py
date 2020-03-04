# -*- coding: utf-8 -*-

def df(x):
    fact = [1,1,2,6,24,120,720,5040,40320,362880]
    return sum( [fact[int(i)] for i in str(x)] )

i = 1
totchain = 0
while i < 1000000:
    chain = []
    temp = i
    while temp not in chain:
        chain.append(temp)
        temp = df( temp )
    if len(chain) ==  60:
        totchain += 1
        print( i, totchain )
    i += 1
    if i % 10000 == 0:
        print( round(i/10000.0,3) )










