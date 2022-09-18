#Tenka1 Programmer Beginner Contest D - Crossing
#三角数、グラフ

#https://babcs2035.hateblo.jp/entry/2018/11/03/143845
#N==1のケース？
#https://drken1215.hatenablog.com/entry/2018/10/29/004900

N = int(input())
mx = 1000
G = [[0]*mx for _ in range(mx)] #前処理用グラフ

r = 0 #数字を入れる行
c = 0 #数字を入れる列
for i in range(1,N+1):
    G[r][c] = i #順番に数字を入れる
    c += 1 #次の列へ移動
    if r < c: #jがi行の上限に到達したら、次の行に移動、列を0にする
        r +=1
        c = 0
#print(*G,sep="\n")
#print(r,c)

ans = []
for i in range(r):
    A = [] #答えを順につくる（解説図の通り？のプログラム）
    for j in range(r):
        if i >= j: #直進
            A.append(G[i][j])
        else: #曲がって再び直進
            A.append(G[j][i])
    ans.append(A)

A = [] #斜めの答え
for i in range(r):
    A.append(G[i][i])
ans.append(A)
#print()
#print(*ans,sep="\n")

if c != 0: #列cが0になっていなければ三角数でない
    print("No")
else:
    print("Yes")
    print(r+1)
    for i in range(r+1):
        print(len(ans[i]), *ans[i])

