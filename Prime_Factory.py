import math

a = int(input())
if a == 1:
    print('no')
else:
    l=[]
    while a % 2 == 0:
        l.append(2)
        a = a // 2
    for i in range(3,int(math.sqrt(a))+1,2):
        while (a % i == 0):
            l.append(i)
            a = a // i

    if a > 2:
        l.append(a)
    l.sort()
    l = set(l)
    if len(l) == 1:
        print('yes')
    else:
        print('no')
    # for i in l:
    #     print('{}'.format(i), end=' ')
    # print()