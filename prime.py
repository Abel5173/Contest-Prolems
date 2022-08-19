def cp(n):
      count = 0
      primes = [False for i in range(n+1)]
      for i in range(2,n+1):
         if primes[i] == False:
            count+=1
            j = 2
            while j*i<n:
               primes[j*i] = True
               j+=1
      return count
n, q = map(int, input().split())
print(cp(n))
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

for i in range(q):
    a = int(input())
    print('1' if is_prime(a) else '0')