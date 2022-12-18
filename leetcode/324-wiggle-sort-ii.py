class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        temp = []
        mid = (len(nums)-1)//2
        l, r = mid, len(nums)-1
        
        while l >= 0 and r > mid:
            temp.append(nums[l])
            temp.append(nums[r])
            l -= 1
            r -= 1
        if l == 0:
            temp.append(nums[l])

        for i in range(len(temp)):
            nums[i] = temp[i]
        
