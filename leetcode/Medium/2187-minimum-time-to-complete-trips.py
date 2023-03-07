class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def need_more_time(curr_time):
            total_trip_cnts = 0
            for t in time:
                total_trip_cnts += curr_time // t
            return total_trip_cnts < totalTrips

        l, r = 1, min(time) * totalTrips #[l, r]
        while l < r:
            mid = (l+r)//2
            if need_more_time(mid):
                l = mid + 1
            else:
                r = mid
        return l
