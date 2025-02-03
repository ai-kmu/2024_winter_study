class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        flag = True #증가중
        counter = 1
        ans = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]: #증가중
                if(flag): 
                    counter += 1
                else: 
                    flag = True
                    counter = 2
            elif nums[i] > nums[i+1]:
                if(not flag): 
                    counter += 1
                else: 
                    flag = False
                    counter = 2
            else:
                counter = 1

            ans = max(ans, counter)

        return ans

