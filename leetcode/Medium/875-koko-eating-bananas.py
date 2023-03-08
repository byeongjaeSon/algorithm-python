class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all_in_time(time):
            needed_time = 0
            for pile in piles:
                needed_time += int(ceil(pile/time))
            return needed_time <= h

        l, r = 1, max(piles)
        while l < r:
            mid = (l+r)//2
            if can_eat_all_in_time(mid):
                r = mid
            else:
                l = mid + 1
                
        return l