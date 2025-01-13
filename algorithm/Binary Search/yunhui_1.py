class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        answer = -1

        while(left < right): 
            mid = (left + right) // 2
            if nums[mid] == target:
                answer = mid 
                break 
            elif nums[mid] > target:
                right = mid 
            elif nums[mid] < target:
                left = mid + 1

        return answer 


