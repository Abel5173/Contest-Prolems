from datetime import datetime
s1 = input()
s2 = input()
s1 = datetime.strptime(s1, '%H:%M:%S')
s2 = datetime.strptime(s2, '%H:%M:%S')
if s1 == s2:
    print('24:00:00')
else:
        tdelta = s2 - s1
        s=str(tdelta)
        l=list(s.split())
        
        a,b,c = (l[-1].split(':'))
        a=int(a)
        b=int(b)
        c=int(c)
        print("{:02d}:{:02d}:{:02d}".format(a,b,c))