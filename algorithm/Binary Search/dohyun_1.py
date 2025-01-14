class Solution(object):
    def search(self, nums, target):
        st = 0
        ed = len(nums)-1
        while st <= ed:
            mid = (st + ed) // 2
            if (nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                ed = mid - 1
            else:
                st = mid + 1
        return -1
