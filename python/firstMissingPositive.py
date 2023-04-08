from typing import List


class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.test()

    def firstMissingPositive(self, nums: List[int]) -> int:
        numbers = sorted(nums)
        i = 0
        while i < len(numbers):
            if numbers[i] > 0:
                break
            i += 1
        numbers = sorted(set(numbers[i:]))
        for j in range(len(numbers)):
            if numbers[j] != j + 1:
                return j + 1
        return len(numbers) + 1

    def test(self):
        print(self.firstMissingPositive(self.nums))


Solution([1,1000])