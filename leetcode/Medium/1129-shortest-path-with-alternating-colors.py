class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        dist = [[-1] * n for _ in range(2)]
        q = deque([(0, 'R'), (0, 'B')])
        dist[0][0] = dist[1][0] = 0
        
        redEdgesMap, blueEdgesMap = defaultdict(list), defaultdict(list)
        for a, b in redEdges:
            redEdgesMap[a].append(b)
        for u, v in blueEdges:
            blueEdgesMap[u].append(v)

        level = 1
        while q:
            qSize = len(q)
            for _ in range(qSize):
                curr_node, before_edge_color = q.popleft()
                if before_edge_color == 'B':
                    for next_node in redEdgesMap[curr_node]:
                        if dist[0][next_node] == -1:
                            dist[0][next_node] = level
                            q.append((next_node, 'R'))
                elif before_edge_color == 'R':
                    for next_node in blueEdgesMap[curr_node]:
                        if dist[1][next_node] == -1:
                            dist[1][next_node] = level
                            q.append((next_node, 'B'))
            level += 1
        
        answer = [0] * n
        for i in range(n):
            if dist[0][i] == -1 and dist[1][i] == -1:
                answer[i] = -1
            elif dist[0][i] == -1:
                answer[i] = dist[1][i]
            elif dist[1][i] == -1:
                answer[i] = dist[0][i]
            else:
                answer[i] = min(dist[0][i], dist[1][i])
        return answer
