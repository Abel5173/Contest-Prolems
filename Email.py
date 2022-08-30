n = int(input())
for i in range(n):
    a, b = map(str, input().split())
    b = b.lower()
    a = a[0].lower()
    print(a+b+'@mapcom-group.com')
