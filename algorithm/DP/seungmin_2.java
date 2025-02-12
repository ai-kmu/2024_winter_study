// 핵심 : 각 자리 n에서 어떤 글자로 시작할 수 있는지 알면 --> 이전 단계 n-1에서 가능한 개수 다 합해서 구할 수 있음. 이 걸 dp적용함
class Solution {
    public int countVowelStrings(int n) {
        
        // 0부터 n까지 사용
        int[][] dp = new int[n + 1][5];

        // 초기값 설정 - n=1일 때는 aeiou 1개씩
        for (int j = 0; j < 5; j++) {
            dp[1][j] = 1;
        }

        // DP
        // 길이가 2부터 시작
        for (int i = 2; i <= n; i++) {
            // 첫 글자가 a ~ u일 때
            for (int j = 0; j < 5; j++) {
                // 사전 순서를 지키는 범위 내에서
                for (int t = j; t < 5; t++) {
                    // dp 핵심
                    dp[i][j] = dp[i][j] + dp[i - 1][t];
                }
            }
        }
        
        int result = 0;
        for (int j = 0; j < 5; j++) {
            result = result + dp[n][j];
        }
        
        return result;
    }
}
