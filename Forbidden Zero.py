n = int(input())
if (n+1) % 10 == 0:
    n += 1
    l = str(n).count('0') - 1
    while l >= 0:
        n += (10**l)
        l -= 1
    print(n)
else:
    print(n+1)