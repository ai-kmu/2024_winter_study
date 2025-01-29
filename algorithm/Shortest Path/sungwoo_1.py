class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

class Solution:
    def validPath(self, n, edges, source, destination):
        uf = UnionFind(n)
        
        for a, b in edges:
            uf.union(a, b)
        
        return uf.find(source) == uf.find(destination)
