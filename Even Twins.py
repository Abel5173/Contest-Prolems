n = int(input())
l = [int(i) for i in input().split()]
m = []
for i in range(1, n):
    if (l[i-1] + l[i]) % 2 == 0:
        m.append(l[i-1] + l[i])
if len(m) == 0:
    print('NULL')
else:
    print(*m)
    