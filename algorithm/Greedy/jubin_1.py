class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        result_list = []
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    result_list.append(i)
                    result_list.append(j)
                    break
            if result_list:
                break

        return result_list
