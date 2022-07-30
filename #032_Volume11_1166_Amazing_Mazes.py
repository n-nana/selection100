#AOJ_Volume11_1166_Amazing Mazes
#https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1166&lang=ja
#BFS

from collections import deque

while True:
    W,H = map(int,input().split())
    if W == 0 and H == 0: break
    
    res = [[0]*W for _ in range(H)]
    E = [[[] for i in range(W)] for j in range(H)]
    for i in range(2*H-1):
        A = list(map(int,input().split()))
        
        if i%2 == 0:
            y = i//2
            for j in range(W-1):
                if A[j] == 0:
                    x1,x2 = j,j+1
                    E[y][x1].append([y,x2])
                    E[y][x2].append([y,x1])
        elif i%2 == 1:
            y1 = i//2
            y2 = i//2 + 1
            for j in range(W):
                if A[j] == 0:
                    x = j
                    E[y1][x].append([y2,x])
                    E[y2][x].append([y1,x])
    
    deq = deque()
    deq.append([0,0])
    res[0][0] = 1
    
    while len(deq) > 0:
        cy,cx = deq.popleft()
        for ny,nx in E[cy][cx]:
            if res[ny][nx] != 0: continue
            deq.append([ny,nx])
            res[ny][nx] = res[cy][cx] + 1
    
    print(res[-1][-1])

