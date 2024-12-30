class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_to_str = str(x)
        xlist = list(x_to_str)

        if xlist == xlist[::-1]:
            return True
        else:
            return False
