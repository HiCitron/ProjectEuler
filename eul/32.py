# -*- coding: utf-8 -*-

def IN(prod, tab):
    for i in range( len(tab) ):
        tab[i] = str( tab[i] )
    prod = str(prod)
    for i in range( len(prod) ):
        if prod[i] not in tab:
            return False
        else:
            for k in range( len(tab) ):
                if tab[k] == prod[i]:
                    tab.pop(k)
                    break
    return p1
        

t = [1,2,3,4,5,6,7,8,9]
temp0 = []
for a1 in range( len(t) ):
    temp1 = t[:]
    c1 = temp1.pop(a1)
    print(c1)
    for a2 in range( len(t) - 1 ):
        temp2 = temp1[:]
        c2 = temp2.pop(a2)
        for a3 in range( len(t) - 2 ):
            temp3 = temp2[:]
            c3 = temp3.pop(a3)
            for a4 in range( len(t) - 3 ):
                temp4 = temp3[:]
                c4 = temp4.pop(a4)
                for a5 in range( len(t) - 4 ):
                    temp5 = temp4[:]
                    c5 = temp5.pop(a5)
                    
                    p1 = (c1*10+c2) * (c3*100+c4*10+c5)
                    p2 = (c1*100+c2*10+c3) * (c4*10+c5)
                    p3 = (c1*1000+c2*100+c3*10+c4) * (c5)
                    p4 = (c1) * (c2*1000+c3*100+c4*10+c5)
                    
                    if IN(p1, temp5):
                        if p1 not in temp0:
                            temp0.append(p1)
                        print( (c1*10+c2), (c3*100+c4*10+c5), p1)
                    if IN(p2, temp5):
                        if p2 not in temp0:
                            temp0.append(p2)
                        print( (c1*100+c2*10+c3), (c4*10+c5), p2)
                    if IN(p3, temp5):
                        if p3 not in temp0:
                            temp0.append(p3)
                        print( (c1*1000+c2*100+c3*10+c4) , (c5), p3)
                    if IN(p4, temp5):
                        if p4 not in temp0:
                            temp0.append(p4)
                        print( (c1) , (c2*1000+c3*100+c4*10+c5), p4)
"""

#this takes about 10 seconds in trinket
def is_pandigital(n, s=9): n=str(n); return len(n)==s and not '1234567890'[:s].strip(n)

p = set()
for i in range(2,  60):
    start = 1234 if i < 10 else 123 
    for j in range(start, 10000//i):
        if is_pandigital(str(i) + str(j) + str(i*j)): p.add(i*j)

print "Sum of products =", sum(p)
"""