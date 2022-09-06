#JOI 2012 本選 4 - 釘
#2次元いもす
#（参考）https://imoz.jp/algorithms/imos_method.html

N,M = map(int,input().split())

RU = [[0]*(N+2) for _ in range(N+2)]

for _ in range(M):
    a,b,x = map(int,input().split())
    a -= 1
    b -= 1
    RU[a][b] += 1
    RU[a][b+1] -= 1
    RU[a+x+1][b] -= 1
    RU[a+x+2][b+1] += 1
    RU[a+x+1][b+x+2] += 1
    RU[a+x+2][b+x+2] -= 1
#print(*RU,sep="\n")
#print()

#横
for i in range(N+1):
    for j in range(1,N+1):
        RU[i][j] += RU[i][j-1]

#縦
for i in range(1,N+1):
    for j in range(N+1):
        RU[i][j] += RU[i-1][j]

#斜め
for i in range(1,N+1):
    for j in range(1,N+1):
        RU[i][j] += RU[i-1][j-1]
#print(*RU,sep="\n")

res = 0
for i in range(N):
    for j in range(N):
        if i < j: continue #この判定なくてもok
        if RU[i][j] > 0: res += 1

print(res)


