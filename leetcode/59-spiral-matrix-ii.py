class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dy = (0, 1, 0 ,-1)
        dx = (1, 0, -1, 0)
        matrix = [[0] * n for _ in range(n)]
        num = 1
        cy, cx, direction = 0, 0, 0

        while num <= n * n:
            matrix[cy][cx] = num
            num += 1

            ny = cy + dy[direction]
            nx = cx + dx[direction]
            if ny < 0 or ny >= n or nx < 0 or nx >= n or matrix[ny][nx] != 0:
                direction = (direction + 1) % 4
                
            cy += dy[direction]
            cx += dx[direction]

        return matrix
