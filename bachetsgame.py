try:
    while True:
            l= list(map(int, input().split()))
            n = l[0]
            m = l[1]
            a = l[2:]
            a.sort()
            b=a[::-1]
            x=0
            cnt=0
            while n > 0:
                while b[x]<=n:
                    n-=b[x]
                    cnt+=1
                x+=1

            if cnt%2!=0:
                print('Stan wins')
            else:
                print('Ollie wins')
except:
    pass