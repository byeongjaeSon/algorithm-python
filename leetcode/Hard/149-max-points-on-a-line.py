class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
            
        max_cnt = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                (x1, y1), (x2, y2) = points[i], points[j]
                cnt = 0
                for point in points:
                    (x, y) = point
                    if (y - y1) * (x2 - x1) == (y2 - y1) * (x - x1):
                        cnt += 1
                max_cnt = max(max_cnt, cnt)

        return max_cnt
