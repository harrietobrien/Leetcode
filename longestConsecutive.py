from typing import List


class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.test()

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        counts = list()
        currCount = 1
        prev = nums[0]
        for n in nums[1:]:
            if prev + 1 == n:
                currCount += 1
                prev = n
            else:
                counts.append(currCount)
                currCount = 1
                prev = n
            if n == nums[-1]:
                counts.append(currCount)
        return max(counts) if counts else 1

    def test(self):
        print(self.longestConsecutive(self.nums))


tests = [[1, 2, 0, 1],
         [100, 4, 200, 1, 3, 2],
         [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
         [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6],
         [1, 2, 0, 1],
         [0],
         [0, 0],
         []]

for test in tests:
    s = Solution(test)
