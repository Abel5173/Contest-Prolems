from math import sqrt
prime = [True for i in range(20000001+1)]
p = 2
while (p * p <= 20000001):
	if (prime[p] == True):
		for i in range(p * p, 20000001+1, p):
			prime[i] = False
	p += 1
lp=[]
for p in range(2, 20000001+1):
	if prime[p]:
		lp.append(p)
twp=[]
for i in range(len(lp)):
	if lp[i]+2==lp[(i+1)%len(lp)]:
		twp.append(lp[i])

try:
	while True:
		n = int(input())-1
		print('({}, {})'.format(twp[n],twp[n]+2))
except:
	pass

