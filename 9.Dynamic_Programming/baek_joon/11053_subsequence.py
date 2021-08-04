# https://www.acmicpc.net/problem/11053

def solution(n, l):
    if n == 0:
        return print(0)
    memo = [1] * n
    for i in range(1, len(l)):
        for j in range(i):
            if l[i] > l[j] and memo[i] < memo[j]+1:
                memo[i] = memo[j]+1
        print(memo)
    print(max(memo))


n = int(input())
l = [*map(int, input().split())]
solution(n, l)
