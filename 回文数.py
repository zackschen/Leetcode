class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :return False
        stack = []
        reversStack = []
        while(x>0):
            i = x%10
            x = x//10
            stack.append(i)
            reversStack.insert(0,i)
        return stack == reversStack

print(Solution().isPalindrome(-121))