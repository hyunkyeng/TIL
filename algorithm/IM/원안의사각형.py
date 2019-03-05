import sys
sys.stdin = open("원안의사각형.txt")

R = int(input())
n = 0
total = 0

while True:
    if n**2 + 1 < R**2 and R**2 < (n+1)**2 + 1:
        break
    else:
        n += 1

for i in range(n):
    total += i+1

print(total * 4)