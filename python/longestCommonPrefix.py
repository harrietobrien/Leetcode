from typing import List


class Solution:
    def __init__(self, strs):
        self.strs = strs
        self.test()

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        n = min(len(s) for s in strs)
        i = 0
        while i < n:
            prev = ""
            for s in strs:
                if not prev:
                    prev = s[i]
                elif s[i] != prev:
                    return prefix
                else:
                    assert(prev == s[i])
            prefix += prev
            i += 1
        return prefix

    def test(self):
        print(self.longestCommonPrefix(self.strs))


strs = [["flower", "flow", "flight"],
["dog","racecar","car"]]
for s in strs:
    Solution(s)

