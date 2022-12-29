class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        cpu_tasks = [(idx, task[0], task[1]) for idx, task in enumerate(tasks)]
        cpu_tasks.sort(key = lambda x: -x[1])
        order = []
        
        curr_time = 0
        scheduler = []
        while len(cpu_tasks) > 0 or len(scheduler) > 0:
            while len(cpu_tasks) > 0 and cpu_tasks[-1][1] <= curr_time:
                task = cpu_tasks.pop()
                heapq.heappush(scheduler, (task[2], task[0]))
            
            if len(scheduler) > 0:
                processing_task = heapq.heappop(scheduler)
                curr_time += processing_task[0]
                order.append(processing_task[1])
            else:
                if len(cpu_tasks) > 0:
                    curr_time = cpu_tasks[-1][1]
        
        return order
