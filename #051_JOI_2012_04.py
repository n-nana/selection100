#JOI 2014 予選 4 - 部活のスケジュール表
# bit DP

MOD = 10007

N = int(input())
S = input()

dct = dict()
for i,v in enumerate("JOI"): dct[v] = i

dp = [[0]*(1<<3) for _ in range(N+5)]
dp[0][1] = 1 #（0日目に）J君参加

for i in range(N):
    p = dct[S[i]] #i日目の責任者
    for u in range(1<<3): #i日目のメンバー
        for v in range(1<<3): #i+1日目のメンバー
            if (v&(1<<p)) == 0: continue #責任者が出席しない場合
            if (u&v) == 0: continue #鍵がない(同一人物が出席しない)場合
            dp[i+1][v] += dp[i][u]
            dp[i+1][v] %= MOD
#print(*dp,sep="\n")

res = 0
for i in range(1<<3):
    res += dp[N][i]
    res %= MOD #最後にMODをとる

print(res)

