from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))

combis = []
for k in range(1, n):
    combis.extend(combinations(arr, k))

cnt = 0
for combi in combis:
    if sum(combi) == s:
        cnt += 1

print(cnt)