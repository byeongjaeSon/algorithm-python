class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_candi = [i for i in range(len(gas)) if cost[i] - gas[i] <= 0]

        while start_candi:
            start_pos = start_candi.pop()
            curr_gas = 0
            curr_pos = start_pos
            while True:
                curr_gas += gas[curr_pos] - cost[curr_pos]
                if curr_gas < 0: break

                curr_pos = (curr_pos + 1) % len(gas)
                if curr_pos == start_pos:
                    return start_pos
                    
        return -1
