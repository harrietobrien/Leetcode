from typing import List


class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.test()

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0  # slow-run pointer
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                continue
            i += 1
            if i != j:
                nums[i] = nums[j]
        return i + 1

    def test(self):
        print(self.removeDuplicates(self.nums))


nums = [1,1,2]
Solution(nums)
