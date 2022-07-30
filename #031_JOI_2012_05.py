#JOI 2012 予選 5 - イルミネーション
#BFS

from collections import deque

W,H = map(int,input().split())

dy  = [-1,0,1,-1,0,1]
dx = [[0,-1,0,1,1,1],[-1,-1,-1,0,1,0]] #y座標別のdxテーブル

G = []
for _ in range(H):
    g = list(map(int,input().split()))
    G.append(g)
    
done = [[False]*W for _ in range(H)]

res = 0
for y in range(H):
    for x in range(W):
        if not (y == 0 or y == H-1 or x == 0 or x == W-1):
            continue
            
        if done[y][x]:
            continue
            
        if G[y][x] == 1: #建物あり
            idx = y%2
            for i in range(6):
                ny,nx = y+dy[i], x+dx[idx][i]
                # 範囲外と接する辺の数だけ飾り付けを追加
                if not (0 <= ny <= H-1 and 0 <= nx <= W-1):
                    res += 1
                    
        elif G[y][x] == 0: #建物なし
            deq = deque()
            done[y][x] = True
            deq.append((y,x))
        
            while len(deq) > 0:
                cy,cx = deq.popleft()
                idx = cy%2
                for i in range(6):
                    ny,nx = cy+dy[i], cx+dx[idx][i]
                    if not (0 <= ny <= H-1 and 0 <= nx <= W-1):
                        continue
                    if done[ny][nx]:
                        continue
                    # 建物と接する辺の数だけ飾り付けを追加
                    if G[ny][nx] == 1:
                        res += 1
                    elif G[ny][nx] == 0:
                        done[ny][nx] = True
                        deq.append((ny,nx))

print(res)


            
