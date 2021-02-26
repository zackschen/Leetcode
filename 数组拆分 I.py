class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        nums.sort()
        x = 0
        for i in range(0,len(nums),2):
            x += nums[i]
        return x

print(Solution().arrayPairSum([1]))