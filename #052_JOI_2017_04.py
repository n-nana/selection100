#JOI 2017 予選 4 - ぬいぐるみの整理
#bit DP & 累積和
#https://yamakasa.net/aoj-no-633/
#https://blog.hamayanhamayan.com/entry/2019/10/27/233512

N,M = map(int,input().split())

A = []
cnt = [0]*(M)
for _ in range(N):
    a = int(input())
    A.append(a-1)
    cnt[a-1] += 1

#前処理（累積和）
rui = [[0]*(M) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        rui[i+1][j] = rui[i][j]
        if A[i] == j:
            rui[i+1][j] += 1
#print(*rui,sep="\n")

dp = [N]*(1<<M)
dp[0] = 0

for i in range(1<<M):
    done = 0 #固定したぬいぐるみの数
    for j in range(M):
        if (i&(1<<j)) != 0: #集合iに要素jが含まれるかどうか
            done += cnt[j]
    
    #遷移STEP
    for nxt in range(M):
        if (i&(1<<nxt)) == 0: #種類（nxt）のぬいぐるみを固定していない場合
            c = cnt[nxt] - (rui[done + cnt[nxt]][nxt] - rui[done][nxt]) #累積和で操作回数カウント
            dp[i|(1<<nxt)] = min(dp[i] + c, dp[i|(1<<nxt)]) #（遷移先の）更新
#print(dp)

ans = dp[(1<<M)-1]
print(ans)


