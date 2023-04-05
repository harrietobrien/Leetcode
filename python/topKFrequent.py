from typing import List


class Solution:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
        self.test()

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict([(n, 0) for n in nums])
        for num in nums:
            freq[num] += 1
        topK = list()
        for _ in range(k):
            # or max(freq, key=freq.get)
            mxf_key = max(freq, key=lambda x: freq[x])
            topK.append(mxf_key)
            del freq[mxf_key]
        return topK

    def test(self):
        print(self.topKFrequent(self.nums, self.k))


nums = [1, 1, 1, 2, 2, 3]
# nums = [-1, -1]
s = Solution(nums, 1)
