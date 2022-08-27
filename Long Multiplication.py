try: 
    while True: 
        n=input() 
        if n=='0': 
            break 
        a, b = map(int, n.split()) 
        c = a*b 
        s = len(str(c))    
        x, y = len(str(a)), len(str(b)) 
        if a == 0 or b == 0: 
            s = max(len(str(a)), len(str(b))) 
          
        print(' '*(s-x) + str(a)) 
        print(' '*(s-y) + str(b)) 
        print(' '*(s - max(x,y)) + '-'*(max(x,y))) 
        l = [] 
        if x > 0 and y > 0: 
            while(b > 0): 
                d = b%10 * a 
                b //=10 
                if d!=0: 
                   l.append(d) 
            if len(l)>1:        
                for i in range(len(l)): 
                    v = s - len(str(l[i]))-i 
                    print(' '*v + str(l[i])) 
                print('-'*s) 
                 
        if c != 0: 
            print(c) 
            print() 
        else: 
            print(' '*(s-1) + f'{c}') 
            print() 
except: 
    pass