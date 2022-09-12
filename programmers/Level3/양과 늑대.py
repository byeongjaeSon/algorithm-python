from collections import defaultdict

def solution(info, edges):
    
    dic = defaultdict(list)
    for edge in edges:
        dic[edge[0]].append(edge[1])
        
    def backtracking(curr, sheep, wolf, path):
        if info[curr]: wolf += 1
        else: sheep += 1
        
        if wolf >= sheep: return 0
        
        next_positions = [child for node in path for child in dic[node] if child not in path]

        max_sheep = sheep
        for next_pos in next_positions:
            path.append(next_pos)
            max_sheep = max(max_sheep, backtracking(next_pos, sheep, wolf, path))
            path.pop()
        
        return max_sheep

    return backtracking(0, 0, 0, [0])
