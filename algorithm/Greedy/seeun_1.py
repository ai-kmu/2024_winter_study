class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lstlen = len(nums)
        anslst = []
        for i in range(lstlen - 1):
            for j in range(i + 1, lstlen):
                if nums[i] + nums[j] == target:
                    anslst.append(i)
                    anslst.append(j)
                    break
        return anslst
