class Solution:
    def check(self, data: list[int], cookies: list[int], index: int) -> int:
        if index >= len(cookies):
            return max(data)
        result = sum(cookies)
        for i in range(len(data)):
            data[i] += cookies[index]
            if max(data) >= min(data) + sum(cookies[index + 1:]):
                result = min(result, max(data))
            else:
                result = min(result, self.check(data=data, cookies=cookies, index=index + 1))
            data[i] -= cookies[index]
        return result

    def distributeCookies(self, cookies: list[int], k: int) -> int:
        if len(cookies) <= k:
            return max(cookies)
        data = [0 for _ in range(k)]
        data[0] = cookies[0]
        return self.check(data=data, cookies=cookies, index=1)
