from math import gcd

def checkConflict1(arrL):
    for i in range(1,len(arrL)):
        if arrL[i][0] < arrL[i-1][1]:
            return False
    return True

def checkConflict2(arrK):
    for i in range(1,len(arrK)):
        if arrK[i][0] < arrK[i-1][1]:
            return False
    for i in range(1,len(arrK)):
        if gcd(arrK[i][2],arrK[i-1][2]) != 1:
            return False
    return True

def checkConflict3(arr1, arr2):
    for i in arr2:
        j = 0
        while arr1[-1][1] > i[0]+j*i[2]:
            for x in range(len(arr1)):
                if arr1[x][0] <= i[0]+j*i[2] or arr1[x][0] <= i[0]+j*i[2] < arr1[x][1] or arr1[x][0] < i[1]+j*i[2] <= arr1[x][1] :
                    return False
            j+=1
    return True

try:
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break 
        l = []
        for i in range(n):
            a, b = map(int, input().split())
            l.append([a,b])
        l.sort()
        k = []
        for i in range(m):
            a, b, d = map(int, input().split())
            k.append([a,b,d])
        if checkConflict1(l) and checkConflict2(k) and checkConflict3(l,k):
            print('NO CONFLICT')
        else:
            print('CONFLICT')
except:
    pass    

# 1 2
# 985684 992049
# 155542 768411 693799
# 847778 916930 136445 