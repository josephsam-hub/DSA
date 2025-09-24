class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for i in nums:
            if i==target:
                a.append(nums.index(i))
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j] == target :
                a.append(j)
                break
        if not a:
            return [-1,-1]
        else:
            return a