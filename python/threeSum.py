from typing import List


class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.test()

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        threeSums = list()
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    threeSums.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return threeSums

    def test(self):
        print(self.threeSum(self.nums))


nums = [[-1, 0, 1, 2, -1, -4],
        [0, 1, 1], [0, 0, 0]]

for n in nums:
    Solution(n)
