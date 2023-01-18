class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, maxSum, curMax, minSum, curMin = 0, nums[0], 0, nums[0], 0
        for num in nums:
            curMax = max(curMax + num, num)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + num, num)
            minSum = min(minSum, curMin)
            total += num
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
