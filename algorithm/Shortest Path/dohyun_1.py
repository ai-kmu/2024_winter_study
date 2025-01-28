class Solution(object):
    def validPath(self, n, edges, source, destination):
        
        isvisit = [False] * n
        graph = [[] for _ in range(n)]

        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])

        def dfs(curr, destination):
            if curr == destination:
                return True
            isvisit[curr] = True
            for i in graph[curr]:
                if isvisit[i] == False and dfs(i, destination):
                    return True
            return False

        return dfs(source, destination)
