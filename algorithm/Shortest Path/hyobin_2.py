class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for time in times:
            graph[time[0]].append((time[2], time[1]))
            
        q = []
        heappush(q, (0, k))
        costs = {}
        
        while q:
            
            cur_cost, cur_node = heappop(q)
            if cur_node not in costs:
                costs[cur_node] = cur_cost
                
                for cost, next_node in graph[cur_node]:
                    next_cost = cur_cost + cost
                    heappush(q,(next_cost, next_node))
        
        for i in range(1, n + 1):
            if i not in costs:
                return - 1
            
        return max(costs.values()) 
