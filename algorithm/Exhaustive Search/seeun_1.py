class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        strlst = [digit for digit in str(x)]
        strlen = len(strlst) - 1
        for i in range(strlen // 2 + 1):
            if strlst[i] != strlst[strlen - i]:
                return False
        return True
