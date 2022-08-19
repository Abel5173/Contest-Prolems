n = int(input())
l = list(map(int, input().split()))
l.sort()
b=True
for i in range(len(l)-2):
    if l[i]+l[i+1] > l[i+2]:
        print('possible')
        b=False
        break
    i=-1
if b:
    print('impossible')