class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n + 1]; // array ans
        
        // 1부터 n까지
        for (int i = 1; i <= n; i++) {
            // [0,1], [2,3], [4,5], ... , [n-1, n]으로 묶어보면, 두 번째 인자의 1의 개수가 첫 번째 인자보다 1개 더 많음
            ans[i] = ans[i / 2] + (i % 2);
        }
        return ans;
    }
}
