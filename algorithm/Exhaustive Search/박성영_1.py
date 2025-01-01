class Solution(object):
    def isPalindrome(self, x):
        word = str(x)
        for i in range(len(word)):
            if word[i] == word[-1-i]:
                pass
            else:
                return False
                break
        return True