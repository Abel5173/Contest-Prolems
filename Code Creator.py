c = 1
while True:
    n = int(input())
    if n == 0:
        break
    t = 1
    k = []
    while t <= n:
        l = []
        a = input() 
        for i in a:
            if i == '\"':
                l.append('\\\"')
            elif i == '\\':
                l.append('\\\\')
            else:
                l.append(i)
        k.append(l)
        t += 1
    print('Case '+str(c)+':\n#include<string.h>\n#include<stdio.h>\nint main(){')
    for i in k:
        s = ''.join(i)
        print('printf(\"'+s+'\\n\");')  
    print('printf("\\n");\nreturn 0;\n}')
    c += 1