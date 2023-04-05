from math import ceil
from typing import List


class Solution:
    def __init__(self, piles, h):
        self.piles = piles
        self.h = h
        self.test()

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kMin = ceil(sum(piles) / h)
        kMax = max(piles)
        left, right = kMin, kMax + 1
        while left < right:
            kMid = int(left + (right - left) / 2)
            time = sum(ceil(pile/kMid) for pile in piles)
            if time <= h:
                right = kMid
            else:
                assert(time > h)
                left = kMid + 1
        return left

    def test(self):
        print(self.minEatingSpeed(self.piles, self.h))


tests = dict()
tests[8] = [3, 6, 7, 11]
tests[5] = [30, 11, 23, 4, 20]
tests[6] = [30, 11, 23, 4, 20]
for h in tests:
    piles = tests[h]
    s = Solution(piles, h)
