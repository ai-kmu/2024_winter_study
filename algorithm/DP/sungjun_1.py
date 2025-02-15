class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)  

        if n == 0: 
            return ans
        
        ans[1] = 1

        for i in range(2, n + 1):  
            ans[i] = ans[i % 2] + ans[i // 2]  

        return ans
