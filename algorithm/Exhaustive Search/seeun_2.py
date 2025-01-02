import math

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if len(cookies) == k:
            return max(cookies) 

        result = math.inf

        def cookieRec(index, child):
            nonlocal result 

            if index == len(cookies):
                result = min(result, max(child))
                return

            for i in range(k):
                child[i] += cookies[index]

                if max(child) < result:
                    cookieRec(index + 1, child)

                child[i] -= cookies[index]

                if child[i] == 0:
                    break

        cookieRec(0, [0] * k)
        return result

