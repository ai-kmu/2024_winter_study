class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        if n == 0:
            return 0
        
        visited = [False] * n
        minHeap = [(0, 0)]
        total_cost = 0
        count = 0
        
        while minHeap and count < n:
            cost, i = heapq.heappop(minHeap)
            if visited[i]:
                continue
            visited[i] = True
            total_cost += cost
            count += 1
            
            x1, y1 = points[i]
            for j in range(n):
                if not visited[j]:
                    x2, y2 = points[j]
                    d = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minHeap, (d, j))
                    
        return total_cost
