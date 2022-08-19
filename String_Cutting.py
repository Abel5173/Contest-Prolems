t=int(input())
while t>0:
    n=int(input())
    l=list(map(int, input().split()))
    s=input()
    n += (n-1)*2
    print(n)
    t-=1