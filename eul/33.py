# -*- coding: utf-8 -*-


for a in range(1,10):
    for b in range(1,10):
        if b != a:
            for c in range(1,10):
                if c != a and c != b:
                    if (a*10+c)*1.0/ (b*10 + c) == (a *1.0/ b):
                        print( (a*10 + c) , (b*10 + c) , (a * 1.0/b ) )
                    if (c*10+a)*1.0/ (b*10 + c) == (a *1.0/ b):
                        print( (c*10+a) , (b*10 + c) , (a * 1.0/b ) )
                    if (a*10+c)*1.0/ (c*10 + b) == (a *1.0/ b):
                        print( (a*10+c) , (c*10 + b) , (a * 1.0/b ) )
                    if (c*10+a)*1.0/ (c*10 + b) == (a *1.0/ b):
                        print( (c*10+a) , (c*10 + b) , (a * 1.0/b ) )