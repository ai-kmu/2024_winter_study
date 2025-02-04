class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        result = 0
        n = len(nums)

        inc_cnt = 1
        dec_cnt = 1

        if n == 1:
            return 1

        for i in range(n-1):
            if nums[i] < nums[i+1]:
                inc_cnt += 1
            else:
                inc_cnt = 1
            
            if nums[i] > nums[i+1]:
                dec_cnt += 1
            else:
                dec_cnt = 1
            
            result = max(result, dec_cnt, inc_cnt)
        
        return result
