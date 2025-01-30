import java.util.*;

class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        // adjacent list
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] time : times) {
            graph.get(time[0] - 1).add(new int[]{time[2], time[1] - 1});
        }


        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, k - 1});
        int[] distances = new int[n];
        Arrays.fill(distances, Integer.MAX_VALUE);
        boolean[] visited = new boolean[n];

        // shortest path - 다익스트라
        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int distance = current[0];
            int node = current[1];

            if (!visited[node]) {
                visited[node] = true;
                distances[node] = distance;

                for (int[] edge : graph.get(node)) {
                    if (!visited[edge[1]]) {
                        pq.add(new int[]{distance + edge[0], edge[1]});
                    }
                }
            }
        }

        // 최댓값 찾기
        int maxValue = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            maxValue = Math.max(maxValue, distances[i]);
        }
        // result
        return (maxValue == Integer.MAX_VALUE) ? -1 : maxValue;
    }
}
