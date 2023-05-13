class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        dy = (-1, 0, 1, 0)
        dx = (0, 1, 0, -1)

        def bfs(y, x):
            visited[y][x] = True
            q = deque([(y, x)])
            flip_candi = [(y, x)]
            can_flip = True
            while q:
                cy, cx = q.popleft()
                for d in range(4):
                    ny = cy + dy[d]
                    nx = cx + dx[d]

                    if ny < 0 or ny > m-1 or nx < 0 or nx > n-1:
                        can_flip = False
                        continue

                    if board[ny][nx] == "O" and not visited[ny][nx]:
                        q.append((ny, nx))
                        flip_candi.append((ny, nx))
                        visited[ny][nx] = True
                

            if can_flip:
                for i, j in flip_candi:
                    board[i][j] = "X"

        for y in range(m):
            for x in range(n):
                if board[y][x] == "O" and not visited[y][x]:
                    bfs(y, x)    