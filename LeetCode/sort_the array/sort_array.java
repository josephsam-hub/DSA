class Solution {
    public int[] sortArray(int[] nums) {
        int n=nums.length;
        for(int i=n-1;i>0;i--){
            int max1=0;
            for(int j=0;j<=i;j++){
                if(nums[j]>nums[max1]){
                    max1=j;
                }
            }
            if(max1 != i){
            swap(nums,max1,i);}
        }
        return nums;

    }

    private void swap(int arr[],int i,int j){
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;

    }
}