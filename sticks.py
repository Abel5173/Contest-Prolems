while True:
    n,m=map(int, input().split())
    if n==0 and m==0:
        break
    a,b=map(int, input().split())
    for i in range(1,m):
        a,b=map(int, input().split())
