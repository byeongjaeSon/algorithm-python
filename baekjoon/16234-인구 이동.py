import sys
from collections import deque

dy = [-1, 0 , 1, 0]
dx = [0, 1 , 0, -1]
n, l, r = map(int, sys.stdin.readline().split())
populations = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
moving_day = 0

def bfs(y, x):
    q = deque()
    q.append((y,x))
    visited[y][x] = True

    union = {(y,x)}
    total_population = populations[y][x]

    while q:
        cy, cx = q.popleft()
        for direction in range(4):
            ny = cy + dy[direction]
            nx = cx + dx[direction]
            if ny < 0 or ny >= n or nx < 0 or nx >= n or visited[ny][nx]:
                continue
            if l <= abs(populations[ny][nx] - populations[cy][cx]) <= r:
                union.add((ny, nx))
                visited[ny][nx] = True
                q.append((ny, nx))
                total_population += populations[ny][nx]
    
    population_per_country = total_population // len(union)

    for y, x in union:
        populations[y][x] = population_per_country

    return len(union)

while True:
    visited = [[False] * n for _ in range(n)]
    is_moved = False
    for y in range(n):
        for x in range(n):
            if visited[y][x]: continue
            if bfs(y, x) > 1:
                is_moved = True
    
    if is_moved:
        moving_day += 1
    else: 
        break

print(moving_day)
