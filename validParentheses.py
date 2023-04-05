class Solution:
    def __init__(self, s):
        self.s = s
        self.test()

    def isValid(self, s: str) -> bool:
        matches = {"(": ")", "[": "]", "{": "}"}
        starters = list(matches.keys())
        closers = list(matches.values())
        stack = list()
        for char in s:
            if char in starters:
                stack.append(char)
            elif not stack or stack[-1] \
                    != starters[closers.index(char)]:
                return False
            else:
                stack.pop()
        return not stack

    def test(self):
        print(self.isValid(self.s))


ss = ["()", "()[]{}", "(]"]
for s in ss:
    s = Solution(s)
