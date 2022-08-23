n = int(input())
while True:
    b = str(n)[::-1]
    if str(n) == b:
        print(n)
        break
    n+=1