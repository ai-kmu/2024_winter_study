class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            if target == nums[middle]:
                return middle
            if nums[middle] > nums[end] and (target <= nums[end] or target > nums[middle]):
                start = middle + 1
                continue
            if nums[middle] < nums[start] and (target >= nums[start] or target < nums[middle]):
                end = middle - 1
                continue
            if target > nums[middle]:
                start = middle + 1
                continue
            if target < nums[middle]:
                end = middle - 1
                continue
        return -1
