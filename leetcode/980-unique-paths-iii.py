class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(self, curr_pos, path):
            if grid[curr_pos[0]][curr_pos[1]] == 2:
                if len(path) == empty_cell_cnt:
                    self.path_cnt += 1
                return

            for i in range(4):
                ny = curr_pos[0] + dy[i]
                nx = curr_pos[1] + dx[i]

                if ny < 0 or ny >= m or nx < 0 or nx >= n or grid[ny][nx] == -1:
                    continue
                
                next_pos = (ny, nx)
                if next_pos in path: continue

                path.add(next_pos)
                dfs(self, next_pos, path)
                path.discard(next_pos)

        dy = (-1, 0 , 1, 0)
        dx = (0, 1, 0 , -1)
        m, n = len(grid), len(grid[0])
        empty_cell_cnt, starting_cell = m*n, None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    starting_cell = (i,j)
                elif grid[i][j] == -1:
                    empty_cell_cnt -= 1            
        
        path = {starting_cell}
        self.path_cnt = 0
        dfs(self, starting_cell, path)
        return self.path_cnt
