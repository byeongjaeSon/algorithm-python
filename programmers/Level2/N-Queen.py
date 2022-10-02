def put_queen(pos, n):
    if len(pos) == n: return 1
    
    y = 0 if len(pos) == 0 else pos[-1][0] + 1
    
    ret = 0
    for x in range(n):
        for p in pos:
            if (p[1] == x) or (y - p[0] == abs(p[1] - x)):
                break
        else:
            pos.append((y,x))
            ret += put_queen(pos, n)
            pos.pop()
    return ret
                
def solution(n):
    return put_queen([], n)
