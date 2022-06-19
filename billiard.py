


import math
while True:
    a,b,s,m,n = map(int,input().split())
    if s==0:
        break
    x=a*m
    y=n*b
    print("{:0.2f} {:0.2f}".format(round(math.atan(y/x)*180/math.pi,2),round(math.sqrt(x*x+y*y)/s,2)))
