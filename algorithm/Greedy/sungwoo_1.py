class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in nums_dict:
                return [nums_dict[diff], index]
            nums_dict[num] = index
