class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot(nums, left, right):
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left

        pivot = findPivot(nums, 0, len(nums)-1)

        def biSearch(nums, target, left, right):
            
            if left <= right:
                mid = (left+right)//2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return biSearch(nums, target, left, mid-1)
                else:
                    return biSearch(nums, target, mid+1, right)
            
            else:
                return -1

        left_value = biSearch(nums, target, 0, pivot)
        right_value = biSearch(nums, target, pivot, len(nums)-1)

        if left_value == -1 and right_value == -1:
            return -1
        else:
            return max(left_value, right_value)
