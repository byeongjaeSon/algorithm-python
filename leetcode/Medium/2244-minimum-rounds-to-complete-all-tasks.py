class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        difficulty_to_cnt = Counter(tasks)
        max_task_cnt = difficulty_to_cnt.most_common(1)[0][1]
        dp = [-1] * (10**5+1)
        dp[2] = dp[3] = 1
        
        for i in range(4, max_task_cnt+1):
            if dp[i-2] == -1 and dp[i-3] == -1:
                dp[i] = -1
            elif dp[i-2] == -1 or dp[i-3] == -1:
                dp[i] = max(dp[i-2], dp[i-3]) + 1
            else:
                dp[i] = min(dp[i-2], dp[i-3]) + 1
        
        round_num = 0
        for task_cnt in difficulty_to_cnt.values():
            if dp[task_cnt] == -1:
                return -1
            round_num += dp[task_cnt]

        return round_num
