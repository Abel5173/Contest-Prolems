from re import L


n = int(input())
l = []
for i in range(len(str(n))):
    if n % 10 != 0:
        a = (n % 10)*(10**i)
        l.append(a)
    n //= 10
l.reverse()
l = [str(x) for x in l]
s = ' + '.join(l)
print(s)