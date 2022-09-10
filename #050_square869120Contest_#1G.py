#square869120Contest #1_G - Revenge of Traveling Salesman Problem
#bit DP

INF = float("inf")

N,M = map(int,input().split())

L = [[-1]*N for _ in range(N)] # Upper Limit
G = [[-1]*N for _ in range(N)] # Distance

for _ in range(M):
    u,v,d,t = map(int,input().split())
    G[u-1][v-1] = d
    G[v-1][u-1] = d
    L[u-1][v-1] = t
    L[v-1][u-1] = t

mx = 1<<N
dp = [[INF]*N for _ in range(mx)] #Cost
dp[0][0] = 0

cnt = [[0]*N for _ in range(mx)]
cnt[0][0] = 1

for k in range(mx-1):
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if G[i][j] == -1: continue
            if k&(1<<j) != 0: continue #visited
            nc = dp[k][i] + G[i][j] #next_cost
            if nc > L[i][j]: continue #timeover
            nxt = k|(1<<j)
            if nc < dp[nxt][j]:
                dp[nxt][j] = nc
                cnt[nxt][j] = cnt[k][i]
            elif nc == dp[nxt][j]:
                cnt[nxt][j] += cnt[k][i]
                
if dp[mx-1][0] == INF: print("IMPOSSIBLE")
else: print(dp[mx-1][0], cnt[mx-1][0])
    
