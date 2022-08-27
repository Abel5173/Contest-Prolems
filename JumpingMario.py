n = int(input())
for x in range(1,n+1):
    a = int(input())
    l = [int(i) for i in input().split()]
    high = 0
    low = 0
    if a == 1:
        print('Case {}: {} {}'.format(x, high, low))
    else:
        for i in range(1,a):
            if l[i-1] < l[i]:
                high += 1
            elif l[i-1] > l[i]:
                low += 1
        print('Case {}: {} {}'.format(x, high, low))

