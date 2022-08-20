t = int(input())
try:
    for i in range(1,t+1):
        s=list(map(str, input().split()))
        sum = 0.0
        if len(s) > 2:
            a = int(s[0])
            b = int(s[2])
            sum = (a*0.5)+(b*0.05)
            sum = '{:g}'.format(sum)
            print('Case {}: {}'.format(i, sum))
        else:
            a = float(s[0])
            sum = a*0.5
            sum = '{:g}'.format(sum)
            print(f'Case {i}: {sum}')
    print()
except:
    pass