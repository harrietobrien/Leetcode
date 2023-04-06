import math


class Solution:
    def __init__(self, n):
        self.n = n
        self.test()

    def sumSqrDgt(self, n: int) -> list:
        out = 0
        while n > 0:
            out += math.pow(n % 10, 2)
            n //= 10
        return out

    def isHappy(self, n: int) -> bool:
        prev, next = n, self.sumSqrDgt(n)
        while prev != next:
            next = self.sumSqrDgt(self.sumSqrDgt(next))
            prev = self.sumSqrDgt(prev)
        return next == 1

    def test(self):
        print(self.isHappy(self.n))


n = 2
s = Solution(n)
