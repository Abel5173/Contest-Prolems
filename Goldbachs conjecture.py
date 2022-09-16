def cp(n):
      l = []
      primes = [False for i in range(n+1)]
      for i in range(2,n+1):
         if primes[i] == False:
            l.append(i)
            j = 2
            while j*i<n:
               primes[j*i] = True
               j+=1
      return l

try:   
    while True:
        n = int(input())
        if n == -1:
            break
        l = cp(n)
        a = l[:-1]
        k = {}
        for i in a:
            if (n-i) in a:
                k[abs(i-(n-i))] = [n-i,i]
        v = min(k)
        s = k[v]
        s.sort()
        print(f'{s[0]} {s[1]}')
except:
    pass