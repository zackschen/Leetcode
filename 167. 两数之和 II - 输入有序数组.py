class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        length = len(numbers)
        left = 0
        right = length -1
        while (left < right):
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1,right+1]
            elif sum < target:
                left+=1
            else:
                right-=1

print(Solution().twoSum([1,2,3,4,4,9,56,90],8))