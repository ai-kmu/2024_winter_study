class Solution {
    public int minDistance(String word1, String word2) {
        int row = word1.length();
        int col = word2.length();
      
        int dp[][] = new int[row+1][col+1];
      
        char [] word1arr = word1.toCharArray();
        char [] word2arr = word2.toCharArray();
      
        for(int i = 1 ;i < row+1 ;i++) dp[i][0] = i;
        for(int j = 1; j< col+1;j ++) dp[0][j] = j;
        for(int i = 1 ;i <row+1;i++){
            for(int j= 1; j < col+1;j ++){
                if(word1arr[i-1] == word2arr[j-1]){
                    dp[i][j] = dp[i-1][j-1];
                }else{
                    dp[i][j] += Math.min(dp[i-1][j], Math.min(dp[i-1][j-1], dp[i][j-1]))+1;
                }
            }
        }
        return dp[row][col];
    }
}
