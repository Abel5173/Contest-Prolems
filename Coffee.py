t = int(input())
while t > 0:
    n, p = map(int, input().split())
    d = {}
    z = 100//p
    for i in range(n):
        l = [x for x in input().split()]
        d[l[0]] = l[1:]
    k = []
    for i in range(p):
        l = [x for x in input().split()]
        k.append(l)
    for i in k:
        x = d[i[2]]
        if i[1] == 'small':
            y = int(x[0])
        elif i[1] == 'medium':
            y = int(x[1])
        else:
            y = int(x[2])
        ans = y + z
        if (ans+1) % 5 == 0:
            print(i[0],ans+1)
        elif (ans-1) % 5 == 0:
            print(i[0],ans-1)
        else:
            print(i[0],ans)
    
    t -= 1