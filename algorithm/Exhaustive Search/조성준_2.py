class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        user = [0] * k
        user[0] = cookies[0]

        def dfs(user, num):
            if(num == len(cookies)): return max(user)
            ans = 100001
            for i in range(k):
                user_t = user.copy() #반드시 복사를 이렇게 해주어야 한다.
                user_t[i] += cookies[num]
                ans = min(ans, dfs(user_t, num+1))
            return ans

        return dfs(user, 1)
