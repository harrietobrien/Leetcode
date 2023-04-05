from typing import List


class Solution:

    def __init__(self, board):
        self.board = board
        self.test()

    def isValidList(self, lst):
        for i in range(1, 10):
            if lst.count(str(i)) > 1:
                return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        transpose = [[row[i] for row in board]
                     for i in range(n)]
        subgrids = [[board[(j // 3) * 3 + i // 3][(j % 3) * 3 + i % 3]
                     for i in range(n)] for j in range(n)]
        for i in range(len(board)):
            row, col = board[i], transpose[i]
            if not self.isValidList(row) \
                    or not self.isValidList(col) \
                    or not self.isValidList(subgrids[i]):
                return False
        return True

    def test(self):
        print(self.isValidSudoku(self.board))


boardTrue = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

boardFalse = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

s = Solution(boardTrue)
s = Solution(boardFalse)
