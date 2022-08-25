n, m = map(int, input().split())
l = []
for i in range(n):
    a, b = map(int, input().split())
    l.append([a,b])
l.sort()
k = []
for i in range(m):
    a, b, d = map(int, input().split())
    k.append([a,b,d])
for i in k:
    j = 0
    while l[-1][1] > i[0]+j*i[2]:
        for x in range(len(l)):
            if l[x][0] <= i[0]+j*i[2] or l[x][0] <= i[0]+j*i[2] < l[x][1] or l[x][0] < i[1]+j*i[2] <= l[x][1] :
                print(False)
        j+=1
    print(True)