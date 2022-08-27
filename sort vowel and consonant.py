s = input()
c = []
v = []
l = []
vowel = ['a','e','i','o','u']
for i in s:
    if i in vowel:
        v.append(i)
    else:
        c.append(i)
c.sort()
v.sort()
for i in range(len(s)):
    if s[i] in vowel:
        a = v[0]
        l.append(a)
        v.remove(a)
    else:
        b = c[0]
        l.append(b)
        c.remove(b)
s = ''.join(l)
print(s)