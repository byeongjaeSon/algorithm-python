class Solution:
    def wiggleSort(self, nums: List[int]) -> None:        
        num_to_cnt = [0 for _ in range(5001)]
        acc_cnt, mid_cnt = 0, ceil(len(nums)/2)
        mid_key = 0
        for num in nums:
            num_to_cnt[num] += 1

        for num, cnt in enumerate(num_to_cnt):
            acc_cnt += cnt
            if acc_cnt >= mid_cnt:
                mid_key = num
                break  

        remain_cnt = acc_cnt - mid_cnt
        num_to_cnt[mid_key] -= remain_cnt

        arr1 = deque()
        for i in range(mid_key+1):
            arr1.extendleft([i] * num_to_cnt[i])
        
        arr2 = deque([mid_key] * remain_cnt)
        for j in range(mid_key+1, 5001):
            arr2.extendleft([j] * num_to_cnt[j])
        
        k = 0
        for num1, num2 in zip(arr1, arr2):
            nums[k] = num1
            nums[k+1] = num2
            k += 2
        
        if len(nums)%2 == 1:
            nums[-1] = arr1[-1]
