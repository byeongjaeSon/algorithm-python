class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ans = float('inf')
        def back_tracking(topping_idx, total_cost):
            nonlocal ans

            if abs(target - total_cost) < abs(target - ans):
                ans = total_cost
            elif abs(target - total_cost) == abs(target - ans) and total_cost < ans:
                ans = total_cost

            if total_cost > ans or topping_idx == len(toppingCosts):
                return

            back_tracking(topping_idx+1, total_cost)
            back_tracking(topping_idx+1, total_cost + toppingCosts[topping_idx])
            back_tracking(topping_idx+1, total_cost + 2*toppingCosts[topping_idx])
        
        for base_cost in baseCosts:
            back_tracking(0, base_cost)

        return ans