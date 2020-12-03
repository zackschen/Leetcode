from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(1,n):
            if self.isPrime(i):
                count += 1
        return count

    def isPrime(self,n:int):
        if 1 == n:
            return False
        for i in range(2,int(sqrt(n))+1):
            if n % i == 0:
                return False
        return True

print(Solution().countPrimes(1500000))