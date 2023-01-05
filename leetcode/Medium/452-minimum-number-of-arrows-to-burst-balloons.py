class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])

        arrow_cnt = 0
        target = float('-inf')
        for point in points:
            if point[0] <= target <= point[1]:
                continue
            target = point[1]
            arrow_cnt += 1

        return arrow_cnt
