class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final_pos = [0] * len(nums)
        end_pos = len(nums)-1
        final_pos[end_pos] = end_pos
        for i in range(end_pos-1, -1, -1):
            if nums[i] == 0:
                final_pos[i] = i
                continue

            if i+nums[i] < i+1+nums[i+1]:
                final_pos[i] = final_pos[i+1]
                continue

            ret = final_pos[i+1]
            for j in range(nums[i+1]+2, nums[i]+1):
                if i+j >= len(nums):
                    break
                ret = max(ret, final_pos[i + j])
            final_pos[i] = ret
        
        return final_pos[0] == len(nums)-1

