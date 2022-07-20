#JOI 2009 予選 4 - 薄氷渡り
#DFS

import sys
sys.setrecursionlimit(10**7)

def rec(Y,X,cnt):
    global ans
    cnt += 1
    done[Y][X] = True
    for i in range(4):
        ny,nx = Y+dy[i],X+dx[i]
        if not (0 <= ny < N and 0 <= nx < M): continue
        if G[ny][nx] == 0: continue
        if done[ny][nx]: continue
        rec(ny,nx,cnt)
    ans = max(cnt,ans)
    done[Y][X] = False #氷を元に戻す
    cnt -= 1 #氷を元に戻す
    
M = int(input())
N = int(input())

dy = [0,-1,1,0]
dx = [-1,0,0,1]

G = []
for _ in range(N):
    g = list(map(int,input().split()))
    G.append(g)

ans = 0
for y in range(N):
    for x in range(M):
        if G[y][x] == 0: continue
        done = [[False]*M for _ in range(N)]
        rec(y,x,0)

print(ans)

