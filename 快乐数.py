class Solution:
    def isHappy(self, n: int) -> bool:
        alln = set()

        def getNext(n:int):
            nums = []
            while n > 0:
                nums.append(n % 10)
                n = n // 10
            m = 0
            for i in nums:
                m += i ** 2
            return m

        while (n != 1 and n not in alln):
            alln.add(n)
            n = getNext(n)

        return n==1