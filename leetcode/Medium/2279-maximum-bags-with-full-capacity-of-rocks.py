class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remain_capacity = [capacity[i] - rocks[i] for i in range(len(capacity))]
        remain_capacity.sort()
        full_bag_cnt = 0
        for remain in remain_capacity:
            if remain > additionalRocks: break
            additionalRocks -= remain
            full_bag_cnt += 1
        return full_bag_cnt
