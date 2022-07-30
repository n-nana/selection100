#DPL_DPL_1_C_Knapsack_Problem
#ナップザック問題（制限なし）

N,W = map(int,input().split())

A = []
for _ in range(N):
    v,w = map(int,input().split())
    A.append([v,w])

dp = [[-1]*(W+5) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(W+1):
        v,w = A[i]
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])
        if j+w <= W:
            dp[i+1][j+w] = max(dp[i+1][j]+v, dp[i+1][j+w])

#print(*dp,sep="\n") 
ans = max(dp[-1][:W+1])
print(ans)
