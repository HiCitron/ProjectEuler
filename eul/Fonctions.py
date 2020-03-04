from math import sqrt
from random import randint
import time

prem = [2]

def premier(x):
    i = 0
    while prem[i] <= sqrt(x): 
        if x%prem[i] == 0:
            return False
        i += 1
    return True

def nbdiv(x):
    n = 0
    for i in range(1,x+1):
        if x%i == 0:
            n += 1
    return n

def palin(x):
    x = str(x)
    for i in range(len(x)/2):
        if x[i] != x[-i-1]:
            return False
    return True

def coll(x):
    if x%2 == 0:
        return x/2
    else:
        return 3*x + 1
        
        
def fact(x):
    p = 1
    for i in range(2,x+1):
        p *= i
    return p

def sumdigit(x):
    x = str(x)
    s = 0
    for i in range(len(x)):
        s += int(x[i])
    return s

def div(x,y,n):
    res = "0."
    for i in range(1,n):
        res += str(int((x*10**i)/ y))
    return res

def prob206(x):
    x = str(x)
    if x[18] == '0':
        if x[16] == '9':
            if x[14] == '8':
                if x[0] == '1' and x[2] == '2' and x[4] == '3' and x[6] == '4' and x[8] == '5' and x[10] == '6' and x[12] == '7':
                    return True
    return False

ti = time.clock()
res = [0,0,0]
for k in range(1000):
    for i in range(100000):
        j2 = randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6) + randint(1,6)
        j1 = randint(1,4)+randint(1,4)+randint(1,4)+randint(1,4)+randint(1,4)+randint(1,4)+randint(1,4)+randint(1,4)+randint(1,4)
        if j1>j2:
            res[0] += 1
        elif j2>j1:
            res[2] += 1
        else:
            res[1] +=1
    print(float(k)/10,float(res[0])/(res[0]+res[1]+res[2]))
print(res)
tf = time.clock()
print(tf-ti)
"""
(99.9, 0.57318558)
[57318558, 7071656, 35609786]
(99.9, 0.573226)
[57322600, 7077427, 35599973]
(99.9, 0.57316284)
[57316284, 7070070, 35613646]
(99.9, 0.57305433)
[57305433, 7080206, 35614361]
(99.99, 0.573167846)
[573167846, 70762298, 356069856]
"""



"""
mi = 1010101010
ma = 1389026623
for k in range(390):
    for i in range(1000000):
        a = (k+1000)*10**6 + (i+1000000)
        if prob206(a*a):
            print(a,a*a)
    print(k,a)


p = []
for i in range(1000):
    p.append(0)

for a in range(1,1000):
    for b in range(a,1000):
        for c in range(b,1000):
            if a*a+b*b == c*c and a+b+c < 1000:
                p[a+b+c] += 1
print(p)

u = [1,1]
while u[-1] < 10**999:
    u.append(u[-1]+u[-2])
print(len(u))


"     
maxi = 0
for i in range(2,1000000):
    k = i
    n = 0
    while k != 1:
        k = coll(k)
        n += 1
    if n > maxi:648
        maxi = n
        print(n,i)

x = str(2**1000)
s = 0
for i in range(len(x)):
    s += int(x[i])
print(s)

fid = open('nmb.txt','r')
x = fid.readlines()
s = 0
for i in range(len(x)):
    s += int(x[i][0:20])
s = str(s)
print(s[0:10])

maxi = 0
for i in range(333,1000):
    for k in range(1000):
        if palin(k*i):
            if k*i > maxi:
                print(k,i)
                maxi = k*i

n = 0
k = 0
maxi = 0
while n < 500:
    k += 1
    n = nbdiv(int(k*(k+1)*0.5))
    if n > maxi:
        maxi = n
        print(n,k)
print(k,k*(k+1)*0.5)



ch = ['','1','2','3','4','5','6','7','8','9']
maxi = 0
for n15 in range(10):
    for n14 in range(n15,10):
        for n13 in range(n14,10):
            for n12 in range(n13,10):
                for n11 in range(n12,10):
                    for n10 in range(n11,10):
                        for n9 in range(n10,10):
                            for n8 in range(n9,10):
                                for n7 in range(n8,10):
                                    for n6 in range(n7,10):
                                        for n5 in range(n6,10):
                                            for n4 in range(n5,10):
                                                for n3 in range(n4,10):
                                                    for n2 in range(n3,10):
                                                        for n1 in range(n2,10):
                                                            nombre = ch[n15]+ch[n14]+ch[n13]+ch[n12]+ch[n11]+ch[n10]+ch[n9]+ch[n8]+ch[n7]+ch[n6]+ch[n5]+ch[n4]+ch[n3]+ch[n2]+ch[n1]
                                                            if nbet(nombre) > maxi:
                                                                maxi = nbet(nombre)
                                                                print(nbet(nombre),nombre)


def prod(x):
    x = str(x)
    prod = 1
    for i in range(len(x)):
        prod *= int(x[i])
    return prod
    
def nbet(x):
    n = 0
    while x > 9:
        x = prod(x)
        n+= 1
    return n


maxi = 0
for nombre in range(10000000):
    if nbet(nombre) > maxi:
        maxi = nbet(nombre)
        print(nbet(nombre),nombre)
"""

