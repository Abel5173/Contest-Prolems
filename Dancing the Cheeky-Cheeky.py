t = int(input())
while t > 0:
    s = input()
    x = ''
    for i in range(1,len(s)):
        a = s[i:]
        b = s[:i]
        c = a[:len(b)]
        if c == b:
            x = b
    y = s.replace(x,'')
    # print(y)
    n = len(y)
    for i in range(8):
        print(x[(n)%len(x)], end='')
        n += 1
    print('...')

    t -= 1