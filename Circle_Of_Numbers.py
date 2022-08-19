n,a = map(int,input().split())
if a >= n/2:
    print(int(a-(n/2)))
elif a < n/2:
    print(int(a+(n/2)))