class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        
        graph = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            x = points[i][0]
            y = points[i][1]

            for j in range(n):
                graph[i][j] = abs(points[j][0] - x) + abs(points[j][1] - y)

        nearest = [0 for _ in range(n)]
        distance = graph[0]

        result = 0

        for _ in range(1, n):
            min_val = sys.maxsize
            vnear = -1

            for i in range(1, n):
                if 0 <= distance[i] < min_val:
                    vnear = i
                    min_val = distance[i]
            
            result += distance[vnear]

            for i in range(1, n):
                if graph[vnear][i] < distance[i]:
                    distance[i] = graph[vnear][i]
                    nearest[i] = vnear
            
            distance[vnear] = -1
        
        return result
