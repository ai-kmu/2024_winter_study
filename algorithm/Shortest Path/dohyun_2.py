class Solution(object):
    def networkDelayTime(self, times, n, k):

        table = [float('inf')] * n
        table[k - 1] = 0

        for _ in range(n - 1):
            for st, ed, v in times:
                if table[ed-1] > table[st-1] + v and table[st-1] != float('inf'):
                    table[ed-1] = table[st-1] + v
        
        result = max(table)
        return result if result != float('inf')  else -1
