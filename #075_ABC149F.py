# ABC149F - Surrounded Nodes
# 逆元, DFS
# https://www.youtube.com/watch?v=ni-1A-TKgZI
# https://note.com/omotiti/n/n778a88a6ab68
# https://math.nakaken88.com/textbook/cp-modulo-operation-inverse-element/

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline #これを入れないとTLEだった、
MOD = 10**9 + 7

#--------------------------------------
def rec(crr,pre):
    global ans
    
    ci = [] #crrの周囲にあるsub-treeのサイズ
    for nxt in E[crr]:
        if nxt == pre: continue
        rec(nxt,crr)
        size[crr] += size[nxt]
        ci.append(size[nxt])

    if pre != -1: #par方向のsub-treeを追加
        ci.append(N-size[crr])
#    print(crr,ci)
    now = pow(2,N-1,MOD) - 1 #（crr以外の）全組み合わせ - 全部白の場合
    for c in ci:
        now -= pow(2,c,MOD) - 1 #sub-treeの内、1本にのみ黒があるケース
    ans += now
        
#-------------------------------------
N = int(input())

E = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)

size = [1]*N #（自分がparとなる）sub-treeのサイズ

ans = 0
rec(0,-1)
#print(size)

inv = pow(pow(2,N,MOD), MOD-2, MOD)
ans *= inv
ans %= MOD

print(ans)
