from collections import defaultdict

def solution(game_board, table):
    degrees = (0, 90, 180, 270)
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
    n = len(table)
    def rotate(degree, n):
        temp_table = [[0] * n for _ in range(n)]
        if degree == 0:
            for y in range(n):
                for x in range(n):
                    temp_table[y][x] = table[y][x]
        elif degree == 90:
            for y in range(n):
                for x in range(n):
                    temp_table[y][x] = table[x][n-1-y]
        elif degree == 180:
            for y in range(n):
                for x in range(n):
                    temp_table[y][x] = table[n-1-y][n-1-x]
        elif degree == 270:
            for y in range(n):
                for x in range(n):
                    temp_table[y][x] = table[n-1-x][y]
        
        return temp_table
    
    def make_category(y, x, num):
        visited[y][x] = True
        table[y][x] = num
        for dy, dx in delta:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < n and table[ny][nx] == 1 and not visited[ny][nx]:
                make_category(ny, nx, num)
    
    def dfs(board, y, x, cy, cx):
        visited[cy][cx] = True
        positions.append((cy - y, cx - x))
        for dy, dx in delta:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < n and 0 <= nx < n and board[y][x] == board[ny][nx] and not visited[ny][nx]:
                dfs(board, y, x, ny, nx)
    
    category_num = 1
    visited = [[False] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if table[y][x] == 1 and not visited[y][x]:
                make_category(y, x, category_num)
                category_num += 1       
        
    puzzle_pieces = defaultdict(set)
    for degree in degrees:
        rotated_table = rotate(degree, n)
        visited = [[False] * n for _ in range(n)]
        for y in range(n):
            for x in range(n):
                if rotated_table[y][x] != 0 and not visited[y][x]:
                    positions = []
                    dfs(rotated_table, y, x, y, x)
                    puzzle_pieces[rotated_table[y][x]].add(tuple(positions))

    filled_blank_cnt = 0
    visited = [[False] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if game_board[y][x] == 0 and not visited[y][x]:
                positions = []
                dfs(game_board, y, x, y, x)
                for category_num, puzzle_piece in puzzle_pieces.items():
                    if tuple(positions) in puzzle_piece:
                        filled_blank_cnt += len(positions)
                        del puzzle_pieces[category_num]
                        break

    return filled_blank_cnt     