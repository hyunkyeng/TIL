import sys
sys.stdin = open("피보나치수열.txt")

def fibo(x1, x2):
    global arr
    x = x1 + x2
    arr.append(x)
    if len(arr) <= N-1:
        fibo(x2, x)



N = int(input())
arr = [1, 1]
fibo(1, 1)
print(arr[N-1])
