lng, wdth = map(int, input().split())
if lng == wdth:
    print('{}')
else:
    l = []
    while lng != wdth:
        if lng > wdth:
            l.append(wdth)
            lng -= wdth
        else:
            l.append(lng)
            wdth -= lng
    l.append(lng)
    l = [str(x) for x in l]
    s = ', '.join(l)
    print('{'+ s +'}')
