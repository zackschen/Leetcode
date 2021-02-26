class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        length = len(nums)
        result = []
        for x in range(length):
            for y in range(x + 1, length):
                if nums[x] + nums[y] == target:
                    result.append(x)
                    result.append(y)
                    return result