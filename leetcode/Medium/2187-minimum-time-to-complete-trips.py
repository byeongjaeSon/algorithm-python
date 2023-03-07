class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        curr_time = 0
        total_trip_cnts = 0
        while total_trip_cnts < totalTrips:
            curr_time += 1
            for t in time:
                if curr_time % t == 0:
                    total_trip_cnts += 1
        return curr_time