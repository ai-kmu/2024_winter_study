class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr = [1] + [0] * 4 

        for _ in range(n):
            for j in range(1, 5):
                arr[j] += arr[j - 1]

        return sum(arr)
