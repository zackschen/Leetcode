class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        i = 0
        while(i<=len(nums)-1):
            if nums[i] >= target:
                return i
            else:
                i+=1
        return i



print(Solution().searchInsert([1,3,5,6],0))
