# https://www.acmicpc.net/problem/1904

def recursive(n):
    if n in (1, 2):
        return n
    return recursive(n-1) + recursive(n-2)


def dp(n):
    memo = [1, 2]
    while len(memo) < n:
        i = len(memo)
        memo.append(memo[i-1] + memo[i-2])
        print(memo)
    return memo[-1]


print(recursive(3))
print(recursive(4))
print(recursive(5))

print(dp(5))
