import math
from functools import reduce
from typing import List
from math import prod


class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.test()

    def ON2_productExceptSelf(self, nums: List[int]) -> List[int]:
        products = list(1 for _ in range(len(nums)))
        d = dict()
        for i in range(len(nums)):
            d[i] = nums[:i] + nums[i + 1:]
            # products.append(reduce(lambda x, y: x * y, d[k]))
            products[i] *= math.prod(d[i])
        return products

    def ON_productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = list(1 for _ in range(n))
        premult, postmult = 1, 1
        for i in range(n):
            products[i] = premult
            premult *= nums[i]
        reverse = nums[::-1]
        for j in range(n):
            products[n - j - 1] *= postmult
            postmult *= reverse[j]
        return products

    def test(self):
        print(self.ON_productExceptSelf(self.nums))


nums = [-1, 1, 0, -3, 3]
s = Solution(nums)
