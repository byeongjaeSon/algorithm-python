class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_to_cnt = Counter(nums)
        for cnt in num_to_cnt.values():
            if cnt > 1:
                return True
        return False
