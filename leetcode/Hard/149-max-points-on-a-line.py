class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
            
        max_cnt = 0
        for i in range(n):
            mem = defaultdict(int)
            for j in range(n):
                if i == j: continue
                (x1, y1), (x2, y2) = points[i], points[j]

                gradient = None
                if x1 == x2:
                    gradient = float("inf")
                else:
                    gradient = (y2 - y1) / (x2 - x1)
                mem[gradient] += 1

            max_cnt = max(max_cnt, max(mem.values())+1)
        return max_cnt
