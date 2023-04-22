class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] lprod = new int[n];
        int[] rprod = new int[n];
        lprod[0] = 1;
        for(int i=1;i<n;i++) lprod[i] = lprod[i-1]*nums[i-1];
        rprod[n-1] = 1;
        for(int i=n-2;i>=0;i--) rprod[i] = rprod[i+1]*nums[i+1];
        for(int i=0;i<n;i++) nums[i] = lprod[i]*rprod[i];
        return nums;
    }
}