#ABC150D - Semi Common Multiple
#最小公倍数+α
#https://perogram.hateblo.jp/entry/abc150_d
#https://at274.hatenablog.com/entry/2020/01/15/060000

import math

def LCM(x,y):
    return (x*y)//math.gcd(x,y)

def cnt_two(n):
    c = 0
    while n%2 == 0:
        c += 1
        n //= 2
    return c

#--------------------------------------------------------
N,M = map(int,input().split())
A = list(map(int,input().split()))

d = A[0]//2 #A[i]//2の最小公倍数をとる
num = cnt_two(A[0]) #A[i]に含まれる2の数 ->同じならpを変えて同じ値をつくれる ->異なっていればつくれない

flag = True #一つでも素因数である2の数が違っていればFalse

for i in range(1,N):
    d = LCM(d,A[i]//2)
    k = cnt_two(A[i])
    if num != k: flag = False

if flag: print((M//d+1)//2) #切り上げ操作有り
else: print(0)
 
