class Solution(object):
    def longestMonotonicSubarray(self, nums):
        maxinc = 1
        maxdec = 1
        inc = 1
        dec = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                inc += 1
                maxinc = max(inc, maxinc)
            else:
                inc = 1
            
            if nums[i + 1] < nums[i]:
                dec += 1
                maxdec = max(dec, maxdec)
            else:
                dec = 1

        return max(maxinc, maxdec) 
