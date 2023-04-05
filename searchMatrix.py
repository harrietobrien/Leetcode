from typing import List


class Solution:
    def __init__(self, matrix, target):
        self.matrix = matrix
        self.target = target
        self.test()

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target in matrix[i]:
                # row, col = i, matrix[i].index(target)
                return True
        return False

    def test(self):
        print(self.searchMatrix(self.matrix, self.target))


tests = dict()
tests[3] = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
tests[13] = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
for test in tests:
    s = Solution(tests[test], test)
