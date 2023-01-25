class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(node, node_dist):
            level = 0
            node_dist[node] = level
            q = deque([node])        
            while q:
                level += 1
                q_size = len(q)    
                for _ in range(q_size):
                    curr = q.popleft()
                    neighbor = edges[curr]
                    if neighbor == -1 or node_dist[neighbor] != -1:
                        continue
                    node_dist[neighbor] = level
                    q.append(neighbor)
        
        node1_dist = [-1] * len(edges) 
        node2_dist = [-1] * len(edges) 
        bfs(node1, node1_dist)
        bfs(node2, node2_dist)

        ret = -1
        minDist = float('inf')
        for i in range(len(edges)):
            if node1_dist[i] == -1 or node2_dist[i] == -1:
                continue

            if minDist > max(node1_dist[i], node2_dist[i]):
                minDist = max(node1_dist[i], node2_dist[i])
                ret = i
        return ret
