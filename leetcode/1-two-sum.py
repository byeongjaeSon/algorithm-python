class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def binary_search(lo, hi, target):
            while lo < hi:
                mid = (lo+hi)//2
                if numbers[mid][0] > target:
                    hi = mid
                elif numbers[mid][0] < target:
                    lo = mid+1
                else:
                    return numbers[mid][1] 
            return None

        n = len(nums)
        numbers = [(nums[i], i) for i in range(n)]
        numbers.sort(key = lambda x : x[0])
        for i in range(n):
            remain = target-nums[i]
            if numbers[-1][0] < remain: continue
            j = binary_search(0, n, remain)
            if j != None and i != j:
                return [i, j]
