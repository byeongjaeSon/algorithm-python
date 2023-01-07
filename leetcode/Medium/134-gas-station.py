class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        acc, start_point = 0, 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            acc += g - c
            if acc < 0:
                acc = 0
                start_point = i+1
        
        return start_point
