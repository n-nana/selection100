#逆元
#重複あり組合せ

def ncr(n, r, mod):
    if r > n:
        return 0
    x = 1
    for i in range(r):
        x *= (n-i)
        x *= pow(i+1, mod-2, mod)
        x %= mod
    return x

MOD = 10**9 + 7
N = int(input())
K = int(input())

res = ncr(N+K-1, K, MOD)
print(res)
