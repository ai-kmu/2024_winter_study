class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        l = len(x)
        for i in range(l/2+1):
            if(x[i] != x[l-i-1]):
                return False
        return True