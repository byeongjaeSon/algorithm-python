class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ice_cream_cnt = 0
        for cost in costs:
            if coins < cost:
                break
            coins -= cost
            ice_cream_cnt += 1
        
        return ice_cream_cnt
