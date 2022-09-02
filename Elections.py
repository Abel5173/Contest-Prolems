n = int(input())
for i in range(n):
    l = [int(x) for x in input().split()]
    k = []
    m = max(l)
    if len(set(l)) == 1:
        k.append(1)
        k.append(1)
        k.append(1)
        print(*k)
    else:
        if l.count(m) == 2:
            for j in range(len(l)):
                if m == l[j] :
                    k.append(1)
                else:
                    b = (m - l[j]) + 1
                    k.append(b)
            print(*k)    
        else:
            for j in range(len(l)):
                if m == l[j] :
                    k.append(0)
                else:
                    b = (m - l[j]) + 1
                    k.append(b)
            print(*k)
