class Solution:
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        # 초기값, 다른 함수에 쓸 예정이기 때문에 mutable한 리스트로 변수 생성
        result = [sum(cookies)]

        # 각 아이들의 쿠키 양을 저장하기 위한 리스트
        sums = [0] * k

        # 재귀 함수
        def dfs(i):
            # 모든 쿠키를 분배한 경우 중단
            if i == len(cookies):
                result[0] = min(result[0], max(sums))
                return

            # 현재 최대값이 이미 최솟값 이상이면 탐색 중단
            if max(sums) >= result:
                return

            # i번째 쿠키를 각 아이에게 나눠주는 경우 탐색
            for j in range(k):
                # 이전에 동일한 상태로 탐색했을 가능성 제거함
                if j > 0 and sums[j] == sums[j - 1]:
                    continue

                sums[j] += cookies[i]  # 현재 아이에게 쿠키 추가
                dfs(i + 1)             # 다음 쿠키로 이동
                sums[j] -= cookies[i]  # 백트래킹: 이전 상태로 되돌림


        dfs(0)
        return result[0]
