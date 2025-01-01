class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = []
        y = list(str(x))
        for i in range(len(y)-1,-1,-1):
            z.append(y[i])
        return z == y