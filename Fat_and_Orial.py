t=int(input())
for i in range(1,t+1):
        
        k=1
        n,m,a,b=map(float,input().split())
        a=int(a)
        b=int(b)
        na=n*a
        mb=m*(b+a)
        if b!=0:
            y=(mb-na)/b
        else:
            y=-1    
        if y>=0 and y<=10:
            print("Case #{}: {:.2f}".format(i,y))
        else:
            print("Case #{}: Impossible".format(i))  
            
       