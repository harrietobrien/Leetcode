from typing import List


class Solution:
    def __init__(self, strs):
        self.strs = strs
        self.test()

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for string in strs:
            count = [0 for _ in range(26)]
            for char in string:
                index = ord(char) - ord("a")
                count[index] += 1
            key = tuple(count)
            if key not in groups:
                groups[key] = list()
            groups[key].append(string)
        return [groups[k] for k in groups]

    def test(self):
        print(self.groupAnagrams(self.strs))


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution(strs)
