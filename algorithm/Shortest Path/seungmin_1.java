import java.util.*;
class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        if(source == destination) {
            return true;
        }

        // int [][] graph = new int[n][n];
        List<List<Integer>> graph = new ArrayList<>();

        for(int i =0 ; i<n; i++){
            graph.add(new ArrayList<>());
        }
        // 관계행렬에 edges[][]내용들 넣기 - undirected graph
        for(int[] edge : edges){
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[n];

        q.add(source);
        visited[source] = true;

        // 비지 않을 때 까지 반복
        while(q.isEmpty() == false){
            int node = q.remove();

            if(node == destination){
                return true;
            }
            
            // 이어짐 판별 : graph[i][j]==1 && graph[i][j+1]==1 일때, i,j와 i,j+1은 연결
            // (관계행렬 탐색하면서) 연결되어 있지 않고, 미방문했을 때
            // for (int i = 0 ; i < n ; i++){
            //     if(graph[node][i] == 1 && visited[i] == false){ // undirected라 graph[node][i] == graph[i][node]
            //         visited[i] = true;
            //         q.add(i);
            //     }
            // }
            for (int neighbor : graph.get(node)) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.add(neighbor);
                }
            }
        }
        return false;
        
        // boolean[] visited = new boolean[n];
        // return dfs(graph, source, destination, visited);

    }

    // private boolean dfs(int[][] graph, int node, int destination, boolean[] visited){
    //     if(node == destination) {
    //         return true;
    //     }

    //     for(int i= 0 ; i < graph.length; i++){
    //         if(graph[node][i] == 1 && visited[i] == false){
    //             if(dfs(graph,i,destination, visited) == true){
    //                 return true;
    //             }
    //         }
    //     }
    //     return false;
    // }
}
