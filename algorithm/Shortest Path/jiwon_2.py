import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        nodes = [[] for _ in range(n)]
        for time in times:
            nodes[time[0] - 1].append((time[2], time[1] - 1))
        visited = [False for _ in range(n)]
        edges = [(0, k - 1)]
        distances = [float("inf") for _ in range(n)]
        while len(edges) != 0:
            distance, node = heapq.heappop(edges)
            if not visited[node]:
                visited[node] = True
                distances[node] = distance
                for edge in nodes[node]:
                    heapq.heappush(edges, (distance + edge[0], edge[1]))
        result = max(distances)
        if result == float("inf"):
            return -1
        return result
