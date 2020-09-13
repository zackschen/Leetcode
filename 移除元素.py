from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)-1
        length = len(nums)
        while(i<=j):
            # 从后查询不为val的值
            while (nums[j] == val and j>=0):
                length-=1
                j -= 1
            if nums[i] == val and i < j:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
            i+=1
        print(nums[:length])
        return length


print(Solution().removeElement([4,5],4))