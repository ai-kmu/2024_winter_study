class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        right = 0
        for i in range(n):
            if nums[i] == val:
                while nums[n - right - 1] == val:
                    right += 1
                nums[i] = nums[n - right]
                nums[n - right] = val
                right += 1
        k = n - right
        print(nums)
        print(k)
        return k
