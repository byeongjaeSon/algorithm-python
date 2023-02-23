class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        finished = [False] * len(profits)
        
        while k > 0:
            max_project_profit = 0
            project_index = -1
            for i in range(len(profits)):
                if capital[i] <= w and max_project_profit <= profits[i] and finished[i] == False:
                    max_project_profit, project_index = profits[i], i
            w += max_project_profit
            finished[project_index] = True
            k -= 1

        return w