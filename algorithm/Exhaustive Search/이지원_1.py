class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        data = []
        while x != 0:
            data.append(x % 10)
            x //= 10
        for i in range(len(data) // 2):
            if data[i] != data[len(data) - 1 - i]:
                return False
        return True
