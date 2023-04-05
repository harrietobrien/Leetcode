from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.test()

    def singleNumber1(self, nums: List[int]) -> int:
        # XOR of two equal numbers gives 0
        num = 0
        for i in nums:
            num = i ^ num
        return num

    def singleNumber2(self, nums: List[int]) -> int:
        # dict_items([(4, 1), (1, 2), (2, 2)])
        counts: dict = Counter(nums).items()
        return [k for k, v in counts if v == 1][0]

    def singleNumber3(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)

    def test(self):
        print(self.singleNumber1(self.nums))
        print(self.singleNumber2(self.nums))


nums = [[2, 2, 1], [4, 1, 2, 1, 2], [1]]
for n in nums:
    s = Solution(n)
