def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

while True:
    n = int(input())
    if n == -1:
        break
    else:
        print('{} is PRIME!!'.format(n) if is_prime(n) else '{} is COMPOSITE TT'.format(n))