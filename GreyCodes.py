N = int(input())
for g in range(N):
    n, k = map(int, input().split())
    l = ['0', '1']
    if n == 1:
        b = l[k]
        a = int(b, 2)
        print(a)
    else: 
        for i in range(n-1):
            x = len(l) - 1
            while x >= 0:
                l.append(l[x])
                x -= 1
            for j in range(0, len(l)//2):
                l[j] = '0' + l[j]
            for j in range(len(l)//2, len(l)):
                l[j] = '1' + l[j]
        b = l[k]
        a = int(b, 2)
        print(a)