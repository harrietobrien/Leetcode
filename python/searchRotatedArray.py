from typing import List


class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        self.test()

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

    def test(self):
        print(self.search(self.nums, self.target))


tests = [[[4, 5, 6, 7, 0, 1, 2], 0],
         [[4, 5, 6, 7, 0, 1, 2], 3],
         [[3, 5, 1], 3],
         [[1, 3], 3],
         [[1, 3], 1]]

for n, t in tests:
    s = Solution(n, t)
