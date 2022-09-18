#D - Digit Sum Replace
#https://bondo.hateblo.jp/entry/2019/11/24/152250
#https://drken1215.hatenablog.com/entry/2020/01/25/221900

N = int(input())

ans = 0
rem = 0
for _ in range(N):
    d,c = map(int,input().split())
    ans += c #桁数（減少）分のラウンド数を加算
    rem += d*c
    ans += rem//9 #桁数が変わらないラウンド数を加算
    rem %= 9
#    print(ans,rem)
if rem == 0: ans -= 1 #remが9(0)になる（最後に9人残る）場合の-1
print(ans-1) #1桁（0~9）になれば終了なので-1をいれる


