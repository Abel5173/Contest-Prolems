try:
    while True:
        yy, mm, dd = map(int, input().split('-'))        
        add = int((yy // 100)* 0.75 - 1.25)        
        di = {1: 31, 2: 28, 3: 31, 4: 28, 5: 31, 6: 30, 7: 31, 8: 31, 9: 29, 10: 31, 11: 30, 12: 29}
        if yy % 100 == 0 and mm == 2 and dd + add > 28:
            if di[mm] <= dd+add:
                dd = (dd+add)%di[mm]
                mm = (mm)%12 + 1
            else:
                dd = (dd+add)%di[mm]
        else:
            if di[mm] <= dd+add:
                if mm+1 > 12:
                    mm = (mm)%12 + 1
                    yy += 1
                    dd = (dd+add)%di[mm] + 1
                else:
                    dd = (dd+add)%di[mm] + 1
                    mm = (mm)%12 + 1
            else:
                dd = (dd+add)%di[mm] + 1
        a = str(yy)
        b = str(mm)
        c = str(dd)
        if len(b) == 1:
            b = '0'+b
        if len(c) == 1:
            c = '0'+c
        s = '-'.join([a,b,c])
        print(s)
except:
    pass
