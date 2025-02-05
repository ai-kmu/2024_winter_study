// 복잡도: O(n^2 log n)
// 맨해튼 거리 계산
// 크루스칼
// Union-Find
import java.util.*;

class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        List<int[]> edges = new ArrayList<>();
        
        // 모든 점들 간 거리 계산
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int cost = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                edges.add(new int[]{cost, i, j}); // 비용, 연결할 두 노드
            }
        }

        Collections.sort(edges, (a, b) -> a[0] - b[0]); // 거리 기준 정렬 (MS 트리 크루스칼)

        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i; // 유니온 파인드 초기화

        int totalCost = 0, edgeCount = 0;
        
        // 크루스칼 알고리즘 진행
        for (int[] edge : edges) {
            int cost = edge[0], u = edge[1], v = edge[2];

            // 다른 집합에 속해 있어야 연결 가능
            if (find(parent, u) != find(parent, v)) {
                union(parent, u, v);
                totalCost += cost;
                edgeCount++;

                // MST 완성
                if (edgeCount == n - 1) break;
            }
        }

        return totalCost;
    }

    private int find(int[] parent, int node) {
        if (parent[node] != node) {
            parent[node] = find(parent, parent[node]); // 경로 압축
        }
        return parent[node];
    }

    private void union(int[] parent, int u, int v) {
        int rootU = find(parent, u);
        int rootV = find(parent, v);
        parent[rootU] = rootV; // 하나의 그룹으로 합침
    }
}
