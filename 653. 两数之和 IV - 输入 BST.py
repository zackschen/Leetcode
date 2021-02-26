# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = []
        # self.inOrder(nums,root)
        # length = len(nums)
        # left = 0
        # right = length -1
        # while (left < right):
        #     sum = nums[left] + nums[right]
        #     if sum == k:
        #         return [left+1,right+1]
        #     elif sum < k:
        #         left+=1
        #     else:
        #         right-=1

        return self.find(nums,k,root)

    def find(self,nums:[],k:int,root:TreeNode):
        if not root:return False
        if (k - root.val) in nums:return True
        nums.append(root.val)
        return self.find(nums,k,root.left) or self.find(nums,k,root.right)



    def inOrder(self,nums:[],root:TreeNode):
        if not root:return
        self.inOrder(nums,root.left)
        nums.append(root.val)
        self.inOrder(nums,root.right)

print(Solution().twoSum([1,2,3,4,4,9,56,90],8))