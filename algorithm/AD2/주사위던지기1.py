import sys
sys.stdin = open("주사위던지기1.txt")

def dfs1():


N, M = map(int, input().split())

if M == 1:
    dfs1()