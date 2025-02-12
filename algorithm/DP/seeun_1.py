class Solution:
    def countBits(self, n: int) -> List[int]:
        
        DP = [0 for _ in range(n+1)]
        DP[0] = 0

        offset = 1

        for i in range(1, n+1):
            if i == offset:
                DP[i] = 1
                offset = i*2
            else:
                DP[i] = DP[i-offset//2] + 1
        
        return DP
