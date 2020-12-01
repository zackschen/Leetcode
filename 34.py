class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        if (len(nums) == 0) :
            return [-1,-1]
        begin = 0
        length = len(nums)-1
        end = len(nums)-1
        while (begin < length and nums[begin]<target):
            begin += 1

        while (end >= 0 and nums[end] > target):
            end -= 1

        if (end<begin or (end==begin and not nums[end] == target)):
            return [-1,-1]
        return [begin,end]

print(Solution().searchRange(nums=[2,5],target=1))