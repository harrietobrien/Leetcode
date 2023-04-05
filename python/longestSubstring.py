class Solution:
    def __init__(self, s):
        self.s = s
        self.test()

    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        i = 0
        longest = 0
        for j in range(len(s)):
            while s[j] in substr:
                substr = substr.replace(s[i], "")
                i += 1
            substr += s[j]
            longest = max(longest, j - i + 1)
        return longest

    def test(self):
        print(self.lengthOfLongestSubstring(self.s))


ss = ["abcabcbb", "bbbbb", "pwwkew", " ", "", "aab", "dvdf"]
for string in ss:
    s = Solution(string)
