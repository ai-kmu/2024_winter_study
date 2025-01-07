class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}
        for i in range(len(nums)):
            num = target - nums[i]

            if num in tmp:
                return tmp[num], i

            tmp[nums[i]] = i
        
        return []
