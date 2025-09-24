class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        a=set()
        for i in range(0,len(nums)-1):
            sub=nums[i]+nums[i+1]
            if sub in a:
                return True
            a.add(sub)
        return False
        