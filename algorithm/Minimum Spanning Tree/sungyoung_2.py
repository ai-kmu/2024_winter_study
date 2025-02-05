class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_points = len(points)
        graph = {i: [] for i in range(num_points)}
        
        for i in range(num_points):
            x1, y1 = points[i]
            
            for j in range(i + 1, num_points):
                x2, y2 = points[j]
                manhattan_dist = abs(x1 - x2) + abs(y1 - y2)
                
                graph[i].append((manhattan_dist, j))
                graph[j].append((manhattan_dist, i))
                
        total_cost = 0
        visited_nodes = set()
        min_heap = [(0, 0)]
        
        while len(visited_nodes) < num_points:
            cost, point = heappop(min_heap)
            if point in visited_nodes:
                continue
                
            visited_nodes.add(point)
            total_cost += cost
            
            for neighbor in graph[point]:
                if neighbor[1] not in visited_nodes:
                    heappush(min_heap, neighbor)
                    
        return total_cost