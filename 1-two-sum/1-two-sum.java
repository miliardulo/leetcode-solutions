class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hm = new HashMap<>();
        for(int i=0; i<nums.length; i++){
            int x = nums[i];
            if(hm.containsKey(target-x)) return new int[]{i, hm.get(target-x)};
            hm.put(x,i);
        }
        return new int[]{};
    }
}