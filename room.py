import math


t = int(input())
for x in range(t):
    N, b = map(int, input().split())
    i = 10
    for i in range(10, N):
        k = 0
        s = []
        n = b
        while n >0:
            s.append(n%i)
            n = int(n/i)
        l = [str(integer) for integer in s]
        k = "".join(l[::-1])
        r = int(k)
        if r==N:
            print('Hotel Visit #{}: Base {}'.format(x+1, i))
            break
        
