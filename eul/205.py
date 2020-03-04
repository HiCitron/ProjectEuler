# -*- coding: utf-8 -*-


j1 = []
for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            for d in range(1,7):
                for e in range(1,7):
                    for f in range(1,7):
                        j1.append(a+b+c+d+e+f)
j2 = []
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            for d in range(1,5):
                for e in range(1,5):
                    for f in range(1,5):
                        for g in range(1,5):
                            for h in range(1,5):
                                for i in range(1,5):
                                    j2.append(a+b+c+d+e+f+g+h+i)
j1.sort()       # 6 - 36
j2.sort()       # 9 - 36
j1n = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
j2n = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(j1)):
    j1n[j1[i]] += 1
for i in range(len(j2)):
    j2n[j2[i]] += 1

# But: j2 gagne
t1 = sum(j1n)
t2 = sum(j2n)
res = 0.0
for i in range(len(j1n)-1):
    res += j1n[i] * sum(j2n[i+1:-1])
print(float(res))

