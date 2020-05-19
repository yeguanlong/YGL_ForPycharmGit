N=eval(input())
a,b,c,d=0,0,0,0
for a in range(2,N+1):
    for b in range(2,a):
        for c in range(b,a):
            for d in range(c,a):
                if a*a*a==b*b*b+c*c*c+d*d*d:
                    print("Cube = {},Tripe = ({},{},{})".format(a,b,c,d))
    
