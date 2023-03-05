class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        num_to_positions = defaultdict(list)
        for i, num in enumerate(arr):
            num_to_positions[num].append(i)
       
        def bfs():
            q = deque([0])
            level = 0
            visited = [False] * n
            visited[0] = True

            while q:
                q_size = len(q)
                for _ in range(q_size):
                    curr = q.popleft()
                    if curr == n-1:
                        return level

                    for next in num_to_positions[arr[curr]]:
                        if not visited[next]:
                            visited[next] = True
                            q.append(next)

                    num_to_positions[arr[curr]].clear()

                    for next in [curr-1 ,curr+1]:
                        if 0 <= next < n and not visited[next]:
                            visited[next] = True
                            q.append(next)
                 
                level += 1
            return -1
        
        return bfs()