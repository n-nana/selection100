#ABC106D - AtCoder Express 2
#累積和

N,M,Q = map(int,input().split())

RU = [[0]*(N+3) for _ in range(N+3)]

for _ in range(M):
    l,r = map(int,input().split())
    RU[l][r] += 1

for i in range(1,N+1):
    for j in range(i,N+2):
        RU[i][j] += RU[i][j-1]

for _ in range(Q):
    p,q = map(int,input().split())
    res = 0
    for i in range(p,q+1):
        res += RU[i][q]
    print(res)
    
