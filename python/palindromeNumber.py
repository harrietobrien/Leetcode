class Solution:
    def __init__(self, x):
        self.x = x
        self.test()

    def isPalindrome(self, x: int) -> bool:
        digits = list()
        tmp = x
        count = 0
        while tmp > 0:
            digits.append(tmp % 10)
            tmp //= 10
            count += 1
        i, k = 0, len(digits)
        rev = 0
        while k > 0:
            rev += digits[i] * 10 ** (k - 1)
            i += 1
            k -= 1
        return x == rev

    def test(self):
        print(self.isPalindrome(self.x))


Solution(12321)
