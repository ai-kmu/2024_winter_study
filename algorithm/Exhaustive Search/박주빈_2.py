class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def dfs(index, children):

            if index == len(cookies):
                return max(children)

            min_unfairness = float('inf')

            for i in range(k):
                children[i] += cookies[index]
                min_unfairness = min(min_unfairness, dfs(index + 1, children))
                children[i] -= cookies[index]

            return min_unfairness

        children = [0] * k
        return dfs(0, children)
