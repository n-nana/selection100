#GigaCode 2019 D - 家の建設
#2D累積和

H,W,K,V = map(int,input().split())

A = []
for _ in range(H):
    a = list(map(int,input().split()))
    A.append(a)

RU = [[0]*(W+3) for _ in range(H+3)]
for i in range(H):
    for j in range(W):
        RU[i+1][j+1] =  RU[i+1][j] + RU[i][j+1] + A[i][j] - RU[i][j] #2D累積和
#for i in range(H+3):
#    print(RU[i])
#print()

ans = 0
for x1 in range(W):
    for x2 in range(x1+1,W+1):
        for y1 in range(H):
            for y2 in range(y1+1,H+1):
                L = RU[y2][x2] - RU[y2][x1] - RU[y1][x2] + RU[y1][x1] #土地代
                S = (x2-x1)*(y2-y1) #面積
                P = L + S*K #土地代 + 家代
#                print(L,S,P)
                if P <= V:
                    ans = max(S,ans)
print(ans)
                
