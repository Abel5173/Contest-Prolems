while True:
    l = list(map(int, input().split()))
    a = []
    a.append(l[0])
    for i in l:
        if i not in a:
            a.append(i)
    print(*a)