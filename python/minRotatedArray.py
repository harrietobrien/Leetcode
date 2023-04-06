import sys
from typing import List


class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.test()

    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        currMin = sys.maxsize
        while left <= right:
            mid = int(left + (right - left) / 2)
            currMin = min(nums[mid], currMin)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return currMin

    def test(self):
        print(self.findMin(self.nums))


nums = [[4, 5, 6, 7, 0, 1, 2],
        [3, 4, 5, 1, 2]]
for n in nums:
    s = Solution(n)
