class Solution(object):
    def search(self, nums, target):
        st = 0
        ed = len(nums) - 1
        while st <= ed:
            mid = (st + ed) // 2
            if (nums[mid] == target):
                return mid
            elif(nums[st] <= nums[mid]):
                if(nums[st] <= target < nums[mid]):
                    ed = mid - 1
                else:
                    st = mid + 1
            else:
                if(nums[mid] < target <= nums[ed]):
                    st = mid + 1
                else:
                    ed = mid - 1
        return -1
