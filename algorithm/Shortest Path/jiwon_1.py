class Solution:
    def getParent(self, parents: list[int], node: int) -> int:
        while parents[node] != parents[parents[node]]:
            parents[node] = parents[parents[node]]
        return parents[node]

    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        parents = [i for i in range(n)]
        for edge in edges:
            parents[self.getParent(parents, edge[0])] = self.getParent(parents, edge[1])
        return self.getParent(parents, source) == self.getParent(parents, destination)
