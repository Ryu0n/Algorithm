# https://www.acmicpc.net/problem/12865

# 5 7
# 6 13
# 4 8
# 3 6
# 5 12
# 7 15

# 4 7
# 6 13
# 4 8
# 3 6
# 5 12

# 4 7
# 2 3
# 2 4
# 2 5
# 2 6

N, K = list(map(int, input().split()))
back_packs = list()
for n in range(N):
    W, V = list(map(int, input().split()))
    back_packs.append((W, V))
back_packs.sort(key=lambda back_pack: back_pack[0])

memo = [-1] * (K+1)
for w, v in back_packs:
    if memo[w] < v:
        memo[w] = v
print(memo)

for i, (w1, v1) in enumerate(back_packs):
    for j in range(i+1, len(back_packs)):
        w2, v2 = back_packs[j]
        w = w1 + w2
        if w < len(memo) and memo[w1] + memo[w2] > memo[w]:
            memo[w] = memo[w1] + memo[w2]
        print(memo)

print(max(memo))
