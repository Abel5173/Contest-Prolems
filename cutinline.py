n=int(input())
l=[]
for i in range(n):
    a=input()
    l.append(a)
c=int(input())
for i in range(c):
    x=list(map(str, input().split()))
    if x[0]=='cut':
        l.insert(l.index(x[2]), x[1])
    elif x[0]=='leave':
        l.remove(x[1])
for i in l:
    print(i)