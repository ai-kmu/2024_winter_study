class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

        return biSearch(nums, target, 0, len(nums)-1)
