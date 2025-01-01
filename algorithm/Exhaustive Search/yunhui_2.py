class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        arr = [0] * k 

        def dfs(idx):
            if idx == n:
                return max(arr)
            
            answer = float('inf')

            for i in range(k):
                arr[i] += cookies[idx]
                answer = min(answer, dfs(idx + 1))
                arr[i] -= cookies[idx]

                if arr[i] == 0:
                    break 
            
            return answer 

        return dfs(0)
