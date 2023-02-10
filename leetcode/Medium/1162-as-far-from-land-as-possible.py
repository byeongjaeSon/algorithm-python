class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dy = (-1, 0, 1, 0)
        dx = (0, 1, 0, -1)
        visited = [[False] * n for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i,j))
                    visited[i][j] = True
        
        if len(q) == 0 or len(q) == n*n:
            return -1
        
        dist = -1
        while q:
            qSize = len(q)
            for _ in range(qSize):
                cy, cx = q.popleft()
                for i in range(4):
                    ny = cy + dy[i]
                    nx = cx + dx[i]
                    if ny < 0 or ny >= n or nx < 0 or nx >= n or visited[ny][nx]:
                        continue
                    q.append((ny, nx))
                    visited[ny][nx] = True
            dist += 1
        
        return dist
