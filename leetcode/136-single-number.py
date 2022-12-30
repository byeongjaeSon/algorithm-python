class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_to_cnt = Counter(nums)
        for k, v in num_to_cnt.items():
            if v == 1:
                return k
