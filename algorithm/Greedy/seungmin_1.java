import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        
        // arr -> hashmap
        for(int i = 0 ; i < nums.length; i++){
            hashmap.put(nums[i], i);
        }

        for(int i=0; i<nums.length; i++){
            int wantToFind = target - nums[i];

            if(hashmap.containsKey(wantToFind)&&hashmap.get(wantToFind) != i){
                return new int[] {i, hashmap.get(wantToFind)};
            }
        }
        return new int[0];
    }
}
