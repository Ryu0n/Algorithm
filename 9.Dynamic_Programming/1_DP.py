# fibonacci
# f(n) = f(n-1) + f(n-2)

def fib(n):
    if n in (1, 2):
        return 1
    return fib(n-1) + fib(n-2)


print(fib(3))
print(fib(4))
print(fib(5))

# 재귀를 사용할 경우 많은 계산이 중복됨. -> 비효율적
"""
fib(7) = fib(6) + fib(5)
fib(6) = fib(5) + fib(4)
fib(5) = fib(4) + fib(3)
"""
# 고로 한번 계산된 결과는 memorization
# 이렇게 저장하는 것을 caching 이라고도 한다.


def fib_dp(n):
    """
    탑 다운 방식의 dp
    :param n:
    :return:
    """
    print(memo)
    if n in (1, 2):
        return 1
    if memo[n] > 0:
        return memo[n]
    else:
        memo[n] = fib_dp(n-1) + fib_dp(n-2)
        return memo[n]


n = 10
memo = [-1] * (n+1)
print(fib_dp(n))


def fib_dp_bottom_up(n):
    """
    바텀 업 방식의 dp
    :param n:
    :return:
    """
    memo[1] = memo[2] = 1
    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    print(memo)
    return memo[n]


n = 10
memo = [-1] * (n+1)
fib_dp_bottom_up(n)


# 이항 계수
# nCk = n-1Ck + n-1Ck-1
# n개 중에서 k개를 뽑는 서로 다른 경우의 수
# 특정 원소를 뽑고 남은 n-1개 중에서 k-1개를 뽑은 서로 다른 경우의 수
# 다른 원소를 뽑고 남은 n-1개 중에서 k개를 뽑은 서로 다른 경우의 수

def binomial(n, k):
    # 이 코드도 recursion의 형태이므로 중복 계산 -> 비효율적
    if n == k or k == 0:
        return 1
    return binomial(n-1, k) + binomial(n-1, k-1)


def binomial_dp(n, k):
    # n과 k를 기준으로 memorization 해야하므로 2차원 배열을 사용해야하지만
    # python의 장점을 살려 딕셔너리로 구현해봄
    if n == k or k == 0:
        return 1
    if (n, k) in memo:
        return memo.get((n, k))
    else:
        memo[(n, k)] = binomial_dp(n-1, k) + binomial(n-1, k-1)
        return memo[(n, k)]


memo = dict()
print(binomial(10, 3))
print(binomial_dp(10, 3))


def binomial_dp_bottom_up(n, k):
    for i in range(n):
        for j in range(k):
            if j > i:
                continue
            if i == j: # nCn = 1
                memo[i][j] = 1
            elif j == 0: # nC1 = n
                memo[i][j] = i+1
            else: # nCk = n-1Ck + n-1Ck-1
                memo[i][j] = memo[i-1][j] + memo[i-1][j-1]
            print(i, j, '\n', memo, '\n\n')
    return memo[n-1][k-1]


n = 10
k = 3
memo = []
for i in range(n):
    memo.append([-1] * k)
print(binomial_dp_bottom_up(n, k))
