N, X =map(int, input().split())
C = 0
S = 0
while C < N:
    C+= len(str(X))
    X+= 1
    S += 1
if C == N:
    print(S)
else:
    print(-1)
