import math

def primeFactors(n):
    l=[]
    if n % 2 == 0:
        return l
    for i in range(3,int(math.sqrt(n))+1,2):
            while n % i==0:
                l.append(i)
                n = n/i
    if n > 2:
        l.append(n)
    return l

while True:
    n = int(input())
    if n == -1:
        break
    else:
        a=primeFactors(n)
        b = True
        if len(a)==0:
            b = False
        else:
            for i in a:
                print(i)
                # if i % 10 != 3:
                #     b = False
                #     break
        if b:
            print('{} YES'.format(n))
        else:
            print('{} NO'.format(n))