class Solution:
    def __init__(self, s):
        self.s = s
        self.test()

    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s
             if c.isalpha() or c.isnumeric()]
        return s == s[::-1]

    def test(self):
        print(self.isPalindrome(self.s))


s = "A man, a plan, a canal: Panama"
s = Solution(s)