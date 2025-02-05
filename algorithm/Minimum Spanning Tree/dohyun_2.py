class Solution(object):
    def minCostConnectPoints(self, points):
        num = len(points)
        graph = [[] for _ in range(num)]
      
        for i in range(num):
            for j in range(i + 1, num):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append((cost, j))
                graph[j].append((cost, i))
              
        min_heap = [(0, 0)]
        visited = set()
        total_cost = 0
      
        while len(visited) < num:
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
              
            visited.add(node)
            total_cost += cost
          
            for new_cost, neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (new_cost, neighbor))
                  
        return total_cost
