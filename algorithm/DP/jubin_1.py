class Solution:
    def countBits(self, n: int) -> List[int]:
        
        DP = [0 for _ in range(n+1)]

        k = 0

        for i in range(1, n+1):
            if i == 0:
                DP[i] = 0
            elif i == pow(2, k):
                DP[i] = 1
                k += 1
            else:
                DP[i] = DP[pow(2, k-1)] + DP[i-pow(2, k-1)]
        
        return DP
