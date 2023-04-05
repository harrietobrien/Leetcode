from typing import List


class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        self.test()

    def search(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums)
        while lower < upper:
            mid = int(lower + (upper - lower) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lower = mid + 1
            else:
                assert(nums[mid] > target)
                upper = mid
        return -1

    def test(self):
        print(self.search(self.nums, self.target))


nums = dict()
nums[9] = [-1, 0, 3, 5, 9, 12]
nums[2] = [-1, 0, 3, 5, 9, 12]
for n in nums:
    s = Solution(nums[n], n)
