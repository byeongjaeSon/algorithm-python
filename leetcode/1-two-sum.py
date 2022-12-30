class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        val_to_idx = defaultdict(list)
        for i in range(n):
            val_to_idx[nums[i]].append(i)

        numbers = set(nums)
        for i in range(n):
            remain = target-nums[i]
            if remain in numbers:
                if nums[i] == remain:
                    if len(val_to_idx[remain]) > 1:
                        return val_to_idx[remain][:2]
                else:
                    return [i, val_to_idx[remain][0]]
