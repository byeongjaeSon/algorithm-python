def rotate(m, d):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    if d % 4 == 1:
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
    elif d % 4 == 2:
        for r in range(N):
            for c in range(N):
                ret[N-1-r][N-1-c] = m[r][c]
    elif d % 4 == 3:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][r] = m[r][c]
    else:
        for r in range(N):
            for c in range(N):
                ret[r][c] = m[r][c]

    return ret


def solution(key, lock):
    M, N = len(key), len(lock)
    rotated_keys = [rotate(key, d) for d in range(4)]
    extended_lock = [[0] * (N * 3) for _ in range(N * 3)] 
    for i in range(N, 2 * N):
        for j in range(N, 2 * N):
            extended_lock[i][j] = lock[i - N][j - N]
    
    for lock_y in range(2 * N):
        for lock_x in range(2 * N):
            for rotated_key in rotated_keys:
                
                for key_y in range(M):
                    for key_x in range(M):
                        extended_lock[lock_y + key_y][lock_x + key_x] += rotated_key[key_y][key_x]
                
                if all(extended_lock[i][j] == 1 for i in range(N, 2 * N) for j in range(N, 2 * N)): return True
                
                for key_y in range(M):
                    for key_x in range(M):
                        extended_lock[lock_y + key_y][lock_x + key_x] -= rotated_key[key_y][key_x]
    return False
