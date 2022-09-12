from collections import defaultdict

def solution(info, edges):
    
    dic = defaultdict(list)
    for edge in edges:
        dic[edge[0]].append(edge[1])
        
    def backtracking(curr, sheep, wolf, path):
        if info[curr]: wolf += 1
        else: sheep += 1
        
        if wolf >= sheep: return 0
        
        next_positions = []
        for node in path:
            next_positions.append(dic[node])
        next_positions = sum(next_positions, [])
    
        max_sheep = sheep
        for next_pos in next_positions:
            if next_pos in path: continue
            path.append(next_pos)
            max_sheep = max(max_sheep, backtracking(next_pos, sheep, wolf, path))
            path.pop()
        
        return max_sheep

    return backtracking(0, 0, 0, [0])
