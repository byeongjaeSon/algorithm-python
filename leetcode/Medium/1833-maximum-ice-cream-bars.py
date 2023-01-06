class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        m = max(costs)
        costCnt = [0] * (m + 1)
        for cost in costs:
            costCnt[cost] += 1
        
        ice_cream_cnt = 0
        for cost, cnt in enumerate(costCnt):
            if cnt == 0:
                continue 
                
            if coins >= cost * cnt:
                ice_cream_cnt += cnt
                coins -= cost * cnt
            else:
                ice_cream_cnt += coins // cost
                break
        
        return ice_cream_cnt
