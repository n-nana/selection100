# ABC074D - Restoring Road Network
# Warshall-Floyd
# https://kakedashi-engineer.appspot.com/2020/04/22/abc074d/
# https://ronly.hatenablog.com/entry/2017/10/14/162524

INF = float("inf")

N = int(input())

dist = []
for _ in range(N):
    d = list(map(int,input().split()))
    dist.append(d)

# 道路の要不要check
need = [[True]*N for _ in range(N)]

flag = True # Falseならば地図は正しくない (-1)
for k in range(N):
    for i in range(N):
        for j in range(N):
            # 地図のi-j距離が最短でない場合、
            if dist[i][j] > dist[i][k] + dist[k][j]:
                flag = False
            # 直接距離(i-j)と迂回距離(i-k, k-j)が等しい場合、
            if dist[i][j] == dist[i][k] + dist[k][j]:
                # iとkが別の都市 and kとjが別の都市
                if i != k and k != j:
                    need[i][j] = False

res = 0
for i in range(N):
    for j in range(N):
        if need[i][j] == True:
            res += dist[i][j]
            
# ダブルカウントしているので結果を2で割る
res //= 2
    
#for i in range(N):
#    print(dist[i])

#for i in range(N):
#    print(need[i])

if not flag: print(-1)
else: print(res)


