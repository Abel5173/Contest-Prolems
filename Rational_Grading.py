try:
    while True:
        n, s = input().split()
        if n=='0' and s=='0':
            break
        else:
            x = int(n, base=16) if n[:2]=='0x' else (int(n, base=8) if n[0]=='0' else int(n))
            cnt = 0
            for i in range(int(s)):
                a, b = input().split()
                b = int(b)
                if a == '++i':
                    x+=1
                    if b == x:
                        cnt+=1
                    else:
                        x = b
                elif a == 'i++':
                    if b == x:
                        cnt+=1
                        x+=1
                    else:
                        x = b
                elif a == '--i':
                    x-=1
                    if b == x:
                        cnt+=1
                    else:
                        x = b
                elif a == 'i--':
                    if b == x:
                        cnt+=1
                        x-=1
                    else:
                        x = b
                elif a == 'i':
                    if b == x:
                        cnt+=1
                    x=b
            print('{}'.format(cnt))
except:
    pass                