class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 값과 인덱스 저장
        num_to_index = {}
        
        for index, num in enumerate(nums):
            # x = 현재 숫자에 대해 target에서 뺀 값
            x = target - num
            
            # x가 딕셔너리에 있는지 확인
            if x in num_to_index:
                # 있다면 현재 인덱스와 x의 인덱스를 반환
                return [num_to_index[x], index]
            
            # 현재 숫자 딕셔너리에 추가
            num_to_index[num] = index