import sys
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, k)]  # (소요 시간, 현재 노드)
        dist = [sys.maxsize] * (n + 1)
        dist[k] = 0

        while pq:
            time, node = heapq.heappop(pq)
            if time > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                new_time = time + weight
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))

        max_time = max(dist[1:])
        
        if max_time != sys.maxsize:
            return max_time
        else:
            return -1
