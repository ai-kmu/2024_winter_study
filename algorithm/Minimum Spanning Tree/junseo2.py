from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0


        min_cost = 0
        visited = set()
        min_heap = [(0, 0)]  
        
        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)  
            if i in visited:
                continue
            
            visited.add(i)
            min_cost += cost

      
            for j in range(n):
                if j not in visited:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(min_heap, (dist, j))

        return min_cost
