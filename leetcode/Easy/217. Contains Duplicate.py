from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for num in nums:
            if d[num]:
                return True
            d[num] += 1
        return False