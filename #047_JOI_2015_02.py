#JOI 2015 本選 2 - ケーキの切り分け 2
#区間DP
#https://9871225.hatenablog.com/entry/2020/07/13/235147

N = int(input())

A = []
for _ in range(N):
    a = int(input())
    A.append(a)
A += A

dp = [[0]*(3*N +3) for _ in range(2*N +3)]
#dp = [[0]*(2*N +3) for _ in range(2*N +3)]

#無からケーキをつくると考える
if N%2 != 0: # 初期値（JOIの1手目のスコア）
    for i in range(2*N):
        dp[i][i] = A[i]
        
turn = (N-1)%2 #Nが奇数の場合、初期値でJOIの1手目済み
for k in range(1,N): #ケーキのサイズ
    for i in range(2*N): #始点
        j = i + k #終点
#        if 2*N <= j: continue #dpの列を2*Nにする場合はこれを入れる
        if turn%2 != 0: #JOI（区間DP）
            dp[i][j] = max(dp[i+1][j]+A[i%N], dp[i][j-1]+A[j%N])
        else: #IOI（貪欲法）
            if A[i] > A[j%N]:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = dp[i][j-1]
    turn = 1 - turn #turn交代(0 or 1)

#print(*dp,sep="\n")
ans = 0
for i in range(N):
    ans = max(dp[i][i+N-1], ans)
print(ans)




