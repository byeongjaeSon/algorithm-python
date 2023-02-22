class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(ship_capacity):
            needed_days, curr_capacity = 1, 0
            for w in weights:
                curr_capacity += w
                if curr_capacity > ship_capacity:
                    needed_days += 1
                    curr_capacity = w
            return days >= needed_days

        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l