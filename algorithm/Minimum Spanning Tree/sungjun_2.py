class Solution:
    def return_dist(self, x1, y1, x2, y2):
        return abs(y2 - y1) + abs(x2 - x1)

    def find(self, v1):
        if self.visited[v1] < 0:
            return v1
        self.visited[v1] = self.find(self.visited[v1])  # 경로 압축
        return self.visited[v1]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 == root2:
            return True

        if self.visited[root1] < self.visited[root2]:  # Union by rank
            self.visited[root2] = root1
        elif self.visited[root1] > self.visited[root2]:
            self.visited[root1] = root2
        else:
            self.visited[root2] = root1
            self.visited[root1] -= 1  # rank 증가
        return False

    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        self.visited = [-1] * len(points)
        self.graph = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                self.graph.append((self.return_dist(points[i][0], points[i][1], points[j][0], points[j][1]), i, j))

        self.graph.sort()
        edges = 0
        ans = 0

        for dist, a, b in self.graph:
            if edges == len(points) - 1:
                break
            if self.union(a, b):
                continue
            ans += dist
            edges += 1

        return ans
