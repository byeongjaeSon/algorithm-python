class Solution:
    def minJumps(self, arr: List[int]) -> int:

        if len(arr) > 1 and arr[0] == arr[-1]:
            return 1
        elif len(arr) > 2 and arr[0] == arr[-2]:
            return 2

        int_to_positions = defaultdict(list)
        for i, num in enumerate(arr):
            int_to_positions[num].append(i)
        
        adj_list = defaultdict(list)
        for i, num in enumerate(arr):
            adj_list[i].extend(int_to_positions[num])
            if i-1 >= 0:
                adj_list[i].append(i-1)
            if i+1 < len(arr):
                adj_list[i].append(i+1)
        
        def dijkstra(n, adj_list):
            dist = [float('inf')] * n
            dist[0] = 0
            pq = []
            heapq.heappush(pq, (dist[0], 0))

            while pq:
                curr_dist, curr_idx = heapq.heappop(pq)

                if curr_dist > dist[curr_idx]:
                    continue
                
                for next_idx in adj_list[curr_idx]:
                    if curr_idx == next_idx:
                        continue

                    if curr_dist + 1 < dist[next_idx]:
                        dist[next_idx] = curr_dist + 1
                        heapq.heappush(pq, (dist[next_idx], next_idx))
            
            return dist
        
        dist = dijkstra(len(arr), adj_list)
        return dist[-1]