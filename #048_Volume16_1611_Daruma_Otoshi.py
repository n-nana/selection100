#区間DP
#max関数を使わず、main関数（solution）を使ったらぎりぎりACした
#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1611&lang=jp
#https://kakedashi-engineer.appspot.com/2020/06/17/aoj1611/

def solution():
    res = []
    while True:
        N = int(input())
        if N == 0: break
        
        W = list(map(int,input().split()))
        dp = [[0]*(N+3) for _ in range(N+3)]
    
        for length in range(1,N): #みている範囲の大きさ
            for i in range(N-length): #始点idx
                j = i + length #終点idx
            
                if (length+1)%2 == 1: #次にみる範囲の大きさが奇数（追加で消せない）
                    if dp[i+1][j] > dp[i][j]:
                        dp[i][j] = dp[i+1][j]
                    if dp[i][j-1] > dp[i][j]:
                        dp[i][j] = dp[i][j-1]
#                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                
                else: #次にみる範囲の大きさが偶数
                    if dp[i+1][j-1] == length-1: #両端以外を全て消せる場合
                        dp[i][j] = dp[i+1][j-1]
                        if abs(W[j]-W[i]) <= 1: #さらに両端を消せる場合
                            dp[i][j] += 2
                    for k in range(i+1,j):
                        if dp[i][k] + dp[k+1][j] > dp[i][j]:
                            dp[i][j] = dp[i][k] + dp[k+1][j]
#                        dp[i][j] = max(dp[i][k] + dp[k+1][j], dp[i][j])
    
        ans = dp[0][N-1]     
        res.append(ans)
#        print(ans)
#        print(*dp,sep="\n")
#        print()
    for num in res: print(num)
solution()
