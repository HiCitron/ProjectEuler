# -*- coding: utf-8 -*-
def lperm(seq, er=False):
    p = [seq]
    n = len(seq)
    for k in xrange(0,n-1):
        for i in xrange(0, len(p)):
            z = p[i][:]
            for c in xrange(0,n-k-1):
                z.append(z.pop(k))
                if er==False or (z not in p):
                    p.append(z[:])
    return p

prem = [2]
for k in range(2,10000):
    b = True
    for i in range(len(prem)):
        if k%prem[i] == 0:
            b = False
            break
    if b:
        prem.append(k)

for n1 in range(1,10):
    for n2 in range(n1,10):
        for n3 in range(n2,10):
            for n4 in range(n3,10):
                t = [n1,n2,n3,n4]
                p = lperm(t)
                
                temp = []
                for i in range(len(p)-1):
                    for k in range(i+1,len(p)):
                        if p[i] == p[k]:
                            temp.append(i)

                temp.sort(reverse=True)  
                temp2 = []
                for i in range(len(temp)):
                    if not(temp[i] in temp2):
                        temp2.append(temp[i])

                for i in range(len(temp2)):
                    p.pop(temp2[i])
                    
                sol = []
                for i in range(len(p)):
                    n = str(p[i][0])+str(p[i][1])+str(p[i][2])+str(p[i][3])
                    if int(n) in prem:
                        sol.append(int(n))
                
                if len(sol) >= 3:
                    sol.sort()
                    for i1 in range(len(sol)):
                        for i2 in range(i1+1,len(sol)):
                            for i3 in range(i2+1,len(sol)):
                                if (sol[i1] - sol[i2]) == (sol[i2] - sol[i3]):
                                    print(sol[i1],sol[i2],sol[i3])

                