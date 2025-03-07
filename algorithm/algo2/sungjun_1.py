class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [1] * n
        
        for i in range(1, n):
            maxi = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxi = max(maxi, ans[j])
                    
            ans[i] = maxi + 1
        
        return max(ans)
