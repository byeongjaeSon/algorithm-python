class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, j = 0, 0
        for num in range(1, 2001):
            if i < len(arr) and num == arr[i]:
                i += 1
                continue
            else:
                j += 1
            
            if j == k:
                return num
        