from curses.ascii import isupper


n = input()
l=[]
for i in n:
    if isupper(i):
        l.append(i)
x = ''
x= x.join(l)
print(x.lower())