import sys
sys.stdin = open("1-n까지의합.txt")

def sumnum(x):
    global result
    if x <= N:
        result += x
        sumnum(x+1)



N = int(input())
result = 0
sumnum(1)
print(result)