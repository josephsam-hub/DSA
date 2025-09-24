class Solution {
    public boolean findSubarrays(int[] nums) {
        Set <Integer> array1= new HashSet<>();
        for (int i=0;i<nums.length-1;i++){
            int sub=nums[i]+nums[i+1];
            if (array1.contains(sub)){
            return true;}
            array1.add(sub);
        }
    return false ;
    }
}