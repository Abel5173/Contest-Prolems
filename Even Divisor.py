t = int(input())
while t > 0:
    l = []
    n = int(input())
    for i in range(n):
        p, a = map(int, input().split())
        l.append([p, a])
    sum = 1
    odd = 1
    for i in l:
        sum *= (i[1]+1)
        if i[0]%2 == 1:
            odd *= (i[1]+1)
    print(sum - odd)
    t -= 1