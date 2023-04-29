from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self, root):
        self.root = root
        self.test()

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def print2DTree(self, root, space=0, LEVEL_SPACE=5):
        if not root:
            return
        space += LEVEL_SPACE
        self.print2DTree(root.right, space)
        for i in range(LEVEL_SPACE, space):
            print(end=" ")
        print("|" + str(root.val) + "|<")
        self.print2DTree(root.left, space)

    def test(self):
        invert = self.invertTree(self.root)
        print(self.print2DTree(invert))


# root = [4, 2, 7, 1, 3, 6, 9]
n1 = TreeNode(4)
n2 = n1.left = TreeNode(2)
n3 = n1.right = TreeNode(7)
n4 = n2.left = TreeNode(1)
n5 = n2.right = TreeNode(3)
n6 = n3.left = TreeNode(6)
n7 = n3.right = TreeNode(9)

bt = Solution(n1)
