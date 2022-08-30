try:
    while True:
        n = int(input())
        if n < 1:
            print('0')
        elif n == 1:
            print('1')
        else:
            print(2 * (n-1))
except:
    pass    