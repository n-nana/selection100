#ALDS1_13_A_8 Queens Problem
#順列全探索_permutations

import itertools

dy = [-1,1,-1,1]
dx = [-1,-1,1,1]

N = int(input())

Q = [-1]*8
for _ in range(N):
    r,c = map(int,input().split())
    Q[r] = c

# 初期配置Qとの一致確認
A = list(range(8))
for P in itertools.permutations(A,8):
    flag = True
    for i in range(8):
        if Q[i]!= -1 and Q[i] != P[i]:
            flag = False
            break
     
    # Queenが重ならないかcheck
    if flag:
        for i in range(8):
            if not flag: break
            y,x = i,P[i]
            for d in range(4):
                if not flag: break
                for j in range(1,8): #j=0を飛ばす
                    ny,nx = y+dy[d]*j,x+dx[d]*j
                    if not (0 <= ny < 8 and 0 <= nx < 8): break
                    if P[ny] == nx:
                        flag = False
                        break
                        
    # 問題なければ（flag==True）答えを出力
    if flag:
        res = [["."]*8 for _ in range(8)]
        for y in range(8):
            res[y][P[y]] = "Q"
        for y in range(8):
            print("".join(res[y]))
    
