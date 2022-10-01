from itertools import combinations
import sys

n = int(sys.stdin.readline())

S = [[0] * n for _ in range(n)]
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        S[i][j] = arr[j]

players = {i for i in range(n)}

team1 = list(map(set, combinations(players, n//2)))
team2 = [players - t1 for t1 in team1]

ans = 10**10
for i in range(len(team1)):
    c1, c2 = combinations(team1[i], 2), combinations(team2[i], 2)
    s1, s2 = 0, 0
    for p1, p2 in c1:
        s1 += S[p1][p2] + S[p2][p1]
    for p1, p2 in c2:
        s2 += S[p1][p2] + S[p2][p1]

    ans = min(ans, abs(s1 - s2))

print(ans)