def Sieve(n, q):
    prime = [True for i in range(n+1)]
    p = 2
    prime[1]=False
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    c = 0
    l=[]
    for p in range(2, n):
        if prime[p]:
            c += 1
    l.append(c)
    for i in q:
        if prime[i]:
            l.append(1)
        else:
            l.append(0)
    return l
n, q=map(int, input().split())
l=[]
for i in range(q):
    l.append(int(input()))
x = Sieve(n+1, l)
for i in x:
    print(i)
