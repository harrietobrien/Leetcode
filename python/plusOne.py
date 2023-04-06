from typing import List


class Solution:
    def __init__(self, digits):
        self.digits = digits
        self.test()

    def plusOne(self, digits: List[int]) -> List[int]:
        index = -1
        digits[index] += 1
        while digits[index] % 10 == 0:
            digits[index] = 0
            if index == -len(digits):
                digits.insert(0, 1)
                break
            index -= 1
            digits[index] += 1
        return digits

    def test(self):
        print(self.plusOne(self.digits))


digits = [9]
s = Solution(digits)
