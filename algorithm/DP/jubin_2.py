import math

class Solution:
    def countVowelStrings(self, n: int) -> int:
        result = int(math.factorial(n+4)/(math.factorial(n)*24))
        return result
