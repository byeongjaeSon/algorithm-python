class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        cpu_tasks = [(idx, enqueueTime, processingTime) for idx, (enqueueTime, processingTime) in enumerate(tasks)]
        cpu_tasks.sort(key = lambda x: -x[1])
        order = []
        
        curr_time = 0
        scheduler = []
        while cpu_tasks or scheduler:
            while cpu_tasks and cpu_tasks[-1][1] <= curr_time:
                (idx, _, processingTime) = cpu_tasks.pop()
                heapq.heappush(scheduler, (processingTime, idx))
            
            if scheduler:
                (processingTime, idx) = heapq.heappop(scheduler)
                curr_time += processingTime
                order.append(idx)
            else:
                if cpu_tasks:
                    curr_time = cpu_tasks[-1][1]
        
        return order
