from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
       
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))  
        
        
        min_heap = [(0, k)]  
        shortest_time = {}  
        
        while min_heap:
            time, node = heapq.heappop(min_heap)  
            
            if node in shortest_time: 
                continue
            shortest_time[node] = time  
            
            for neighbor, weight in graph[node]: 
                if neighbor not in shortest_time: 
                    heapq.heappush(min_heap, (time + weight, neighbor))
            

        if len(shortest_time) == n:
            return max(shortest_time.values())  
        return -1  
