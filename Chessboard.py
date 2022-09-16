from math import sqrt

t = int(input())
for i in range(t):
    n = int(input())
    a = n**2 + sqrt(n-1) - 1
    print('{:.3f}'.format(a))
    print()