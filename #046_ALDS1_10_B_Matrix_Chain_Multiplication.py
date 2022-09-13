# ALDS1_10_B_Matrix_Chain_Multiplication
# 区間DP
# https://partender810.hatenablog.com/entry/2020/11/20/105127
# https://qiita.com/mk668a/items/bc5cc36f472487eaf0d8

INF = float("inf")

N = int(input())

A = []
for _ in range(N):
    r,c = map(int,input().split())
    A.append([r,c])

dp = [[INF]*(N+3) for _ in range(N+3)]
for i in range(N+3):
    dp[i][i] = 0

for j in range(N):#左から右
    for i in range(j-1,-1,-1):#下から上
        M = j-i
        for k in range(M+i):#M+i通りの組み合わせ
            dp[i][j] = min(dp[i][k] + dp[k+1][j] + A[i][0]*A[k][1]*A[j][1], dp[i][j])
                    
#print(*dp,sep="\n")
print(dp[0][N-1])

