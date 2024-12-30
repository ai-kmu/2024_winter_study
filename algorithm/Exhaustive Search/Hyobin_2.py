class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        arr = [0 for _ in range(k)]
        arr[0] = cookies[0]

        def dfs(arr, l):
            if l == len(cookies):
                return max(arr)
            
            n = float('inf')

            for i in range(k):
                tmp = arr.copy()
                tmp[i] += cookies[l]
                n = min(n, dfs(tmp, l+1))
            
            return n
        
        return dfs(arr, 1)
