class Solution {
    public boolean canJump(int[] nums) {
        // 우선은 제일 큰 폭으로 뜀
        int start = 0; // 위치
        int destination = nums.length-1; // 끝 위치 index
    
        int location=0;

        for(int i =0 ; i < nums.length; i++){
            int canJump = nums[i];
            if(i > location ){
                return false;
            }
            location = Math.max(location, i + canJump);
            
            if(location >= destination){
                return true;
            }
        }
        return false;
    }
    
}