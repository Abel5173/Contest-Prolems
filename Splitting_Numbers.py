while True:        
    n = int(input())
    if n == 0:
        break
    else:
        n = list(bin(n)[2:])
        l=[]
        for i in range(len(n)):
            if n[i] == '1':
                l.append(i)
        a=[]
        b=[]
        l.sort(reverse=True)
        for i in range(len(l)):
            if i%2==0:
                a.append(l[i])
            else:
                b.append(l[i])
        x=[0]*len(n)
        for i in a:
            x[i]=1
        y=[0]*len(n)
        for i in b:
            y[i]=1
        x1=int("".join(str(i) for i in x),2)
        y1=int("".join(str(i) for i in y),2)
        print(x1, y1)


