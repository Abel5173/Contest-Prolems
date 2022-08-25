arr = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6]
n = [int(a) for a in str(input())]
s = ''.join(map(str, n))
a = sum(n)
for i in n:
    arr.remove(i)
x = 31 - sum(n)
if sum(n) == 31:
    print(s, 'B') if len(n)%2 == 0 else print(s, 'A')
else:
    if x <= 6:
        if x in arr:
            print(s, 'A')  if  len(n)%2 == 0 else print(s, 'B')
        else:
            print(s, 'B')  if  len(n)%2 == 0 else print(s, 'A')

    elif 7 <= x <= 12:
        l = []
        for i in range(1,7):
            d = x - i
            l.append(i)
            if d not in arr:
                print(s, 'B')  if  len(n)%2 == 0 else print(s, 'A')
                break
            else:

    # while x >= 0:
    #     y = max(arr)
        
    #     for i in range(1,7):
    #         if x - i >= 7:
                
    #             cnt = len(n) + 1
    #             x - y   
    #             arr.remove(y)

                