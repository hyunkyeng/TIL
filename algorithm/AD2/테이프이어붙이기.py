import sys
sys.stdin = open("테이프이어붙이기.txt")

def DFS(n, cnt, hap):
    global sol
    if n>=N:
        if cnt == N//2:
            temp = abs(hap-(total-hap))
            if temp < sol:
                sol = temp
        return
    rec[cnt] = data[n]
    DFS(n+1, cnt+1, hap+data[n])
    rec[cnt] = 0
    DFS(n+1, cnt, hap)


N = int(input())
data = list(map(int, input().split()))

rec = [0]*N
sol = 500*20
total = sum(data)
DFS(0, 0, 0)
print(sol)