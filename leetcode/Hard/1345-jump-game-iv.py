class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        int_to_positions = defaultdict(list)
        for i, num in enumerate(arr):
            int_to_positions[num].append(i)
        
        adj_list = defaultdict(set)
        for i, num in enumerate(arr):
            for pos in int_to_positions[num]:
                adj_list[i].add(pos)
            
            if i-1 >= 0:
                adj_list[i].add(i-1)
            if i+1 < len(arr):
                adj_list[i].add(i+1)

        def bfs(adj_list, destination):
            q = deque([0])
            level = 0
            
            while q:
                q_size = len(q)
                for _ in range(q_size):
                    curr = q.popleft()
                    if curr == destination:
                        return level
                    
                    for next in adj_list[curr]:
                        q.append(next)
                level += 1

            return -1
        
        return bfs(adj_list, n-1)