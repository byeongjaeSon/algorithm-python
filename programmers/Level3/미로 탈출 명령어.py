from collections import deque

def solution(n, m, x, y, r, c, k):
    dist = abs(r-x) + abs(c-y)
    if (k - dist) % 2 == 1 or dist > k:
        return "impossible"
    
    delta = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
    q = deque([(x, y)])
    answer = ""
    
    while q:
        cx, cy = q.popleft()
        if cx == r and cy == c and len(answer) == k: break
        for dx, dy, direction in delta:
            nx = cx + dx
            ny = cy + dy
            if nx < 1 or nx > n or ny < 1 or ny > m: continue
            if abs(nx - r) + abs(ny - c) + 1 + len(answer) > k: continue
            q.append((nx, ny))
            answer += direction
            break
    return answer
