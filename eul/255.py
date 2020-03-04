# -*- coding: utf-8 -*-
from math import sqrt

def floor(x):
    return int(x)
def ceil(x):
    if int(x) == x:
        return x
    else:
        return int(x+1)

def dicho( imin, imax, x0 ):
    k = 0
    while imax > imin+1 and k < 20:
        imid = floor((imin+imax)*0.5)
        if rsqrt(imid,x0) == rsqrt(imax,x0):
            imax = imid
        else:
            imin = imid
        k += 1
    return imin;

def rsqrt( n, x0 ):
    x = x0
    x2 = 0
    i = 0
    while abs(x - x2)>0.5:
        x2 = x
        x = floor(0.5*(x2 + ceil(n/x2)))
        i = i + 1
    return i


# Euler 255 > rounded square root

x0 = 7*10**((13-1)*0.5)

xmin = ceil(sqrt(1e13))
xmax = floor(sqrt(1e14)-1)

sumi = 0
for i in range(xmin,xmax+1):
    if i%1000 == 0:
        print(int(10000.0*(i-xmin)/(xmax-xmin+1))/100.0)
    
    imin = ceil( (i-0.5)**2)
    itermin = rsqrt(imin,x0)
    imax = floor((i+0.5)**2)
    itermax = rsqrt(imax,x0)
    
    imid = dicho(imin,imax,x0)
    
    sumi = sumi + ((imid-imin)+1)*itermin + (imax-imid)*itermax


#effets de bords
bmin = xmin^2
bmax = floor((xmin+0.5)**2)
itermin = rsqrt(bmin,x0)
itermax = rsqrt(bmax,x0)
bmid = dicho(bmin,bmax,x0)
sumi = sumi + ((bmid-bmin)+1)*itermin + (bmax-bmid)*itermax


bmin = ceil((xmax+0.5)**2)
bmax = 1e14 - 1
sumi = sumi + ((bmin-bmax)+1)*rsqrt(bmin,x0)


