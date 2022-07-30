#DPL_DPL_1_A_Coin_Changing_Problem

INF = float("inf")

N,M = map(int,input().split())
C = list(map(int,input().split()))

#縦: coinの種類, 横: 総額, 枚数
dp = [[INF]*(N+5) for _ in range(M+1)]
dp[0][0] = 0

for i in range(M):
    c = C[i]
    for j in range(N+1):
        dp[i+1][j] = min(dp[i][j], dp[i+1][j])
        if j+c <= N:
            dp[i+1][j+c] = min(dp[i+1][j]+1, dp[i+1][j+c])

#print(*dp,sep="\n")
print(dp[-1][N])
