s = input()
s = list(s)
sum = 0
cnt = 0
l = []
for i in s:
    if i == 'O':
        cnt += 1
    else:
        l.append(cnt)
        cnt = 0
l.append(cnt)
for i in l:
    sum += (i*(i + 1))//2
print(sum)