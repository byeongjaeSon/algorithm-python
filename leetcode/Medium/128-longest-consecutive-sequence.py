class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num-1 in num_set: 
                continue

            next_num = num + 1
            while next_num in num_set:
                next_num += 1

            max_length = max(next_num - num, max_length)
            
        return max_length
