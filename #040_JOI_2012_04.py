#JOI 2012 予選 4 - パスタ
#DP

MOD = 10000
N,K = map(int,input().split())

fix = [-1]*(N+3) #パスタの種類決定済み
for _ in range(K):
    A,B = map(int,input().split())
    fix[A-1] = B-1
    
dp = [[[0]*3 for i in range(N+3)] for j in range(2)]
# i: 日程, j: 状態 0:翌日も同じものを選べる, 1:翌日は同じものを選べない

# 初日のパスタの種類が決まっているかどうか
if fix[0] == -1:
    for crr in range(3):
        dp[0][0][crr] = 1
else:
    dp[0][0][fix[0]] = 1

    
for i in range(N+1):
    for crr in range(3): #当日のパスタの種類
        for j in range(2):
            if fix[i+1] != -1: #翌日のパスタの種類が決まっている場合、
                nxt = fix[i+1] #パスタの種類
                if crr != nxt: #当日と翌日のパスタの種類が異なる
                    dp[0][i+1][nxt] += dp[j][i][crr]
                else : #パスタの種類が同じ
                    if j == 0: #同じパスタが3日連続にならない
                        dp[1][i+1][nxt] += dp[j][i][crr]
                    
            else: #翌日のパスタの種類が決まっていない場合、
                for nxt in range(3):
                    if crr != nxt:
                        dp[0][i+1][nxt] += dp[j][i][crr]
                    else:
                        if j == 0:
                            dp[1][i+1][nxt] += dp[j][i][crr]
            dp[j][i][crr] %= MOD

res = 0
for crr in range(3):
    for j in range(2):
        res += dp[j][N-1][crr]
        res %= MOD
        
print(res)
#print(dp[0][N-1][:])
#print(dp[1][N-1][:])
