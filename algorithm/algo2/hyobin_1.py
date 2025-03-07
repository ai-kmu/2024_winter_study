import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def lis_length(input_list):
            if not input_list:
                return 0
            
            dp = []
            
            for num in input_list:
                idx = bisect.bisect_left(dp, num)
                if idx == len(dp):
                    dp.append(num)
                else:
                    dp[idx] = num
            
            return len(dp)

        return lis_length(nums)
