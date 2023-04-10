class Solution:
    def __init__(self, n):
        self.n = n
        self.test()

    def climbStairs(self, n: int) -> int:
        i, j = 0, 1
        for _ in range(n):
            i, j = j, i + j
        return j

    def test(self):
        print(self.climbStairs(self.n))


n = 3
Solution(n)
