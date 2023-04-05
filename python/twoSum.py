from typing import List


class Solution:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target
        self.test()

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        rp, lp = len(numbers) - 1, 0
        while lp <= rp:
            if numbers[rp] + numbers[lp] < target:
                lp += 1
            elif numbers[rp] + numbers[lp] > target:
                rp -= 1
            else:
                assert (numbers[rp] + numbers[lp] == target)
                return [lp + 1, rp + 1]

    def test(self):
        print(self.twoSum(self.numbers, self.target))


test = dict()
test[9] = [2, 7, 11, 15]
test[6] = [2, 3, 4]
test[-1] = [-1, 0]
test[8] = [1, 2, 3, 4, 4, 9, 56, 90]

for k in test:
    s = Solution(test[k], k)
