try:
    while True:
        n = int(input())
        l = [int(i) for i in input().split()]
        m = int(input())
        k = []
        k1 = []
        l.sort()
        for i in l:
            for j in l:
                if i + j == m:
                    k.append([i,j])
        minm = 1000001
        b = 0
        for i in k:
            if abs(i[0] - i[1]) <= minm:
                minm = abs(i[0] - i[1])
                b = k.index(i)
        i = min(k[b][0],k[b][1])
        j = max(k[b][0],k[b][1])
        print('Peter should buy books whose prices are {} and {}.'.format(i,j))
        print()

except:
    pass