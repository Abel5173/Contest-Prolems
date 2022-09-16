from math import gcd


try:
    while True:
        a, c, b = map(int, input().split())
        s = gcd((a*c), (b-c))
        x = int((a*c)/s)
        y = int((b-c)/s)
        print(f'{x}/{y}')

except:
    pass