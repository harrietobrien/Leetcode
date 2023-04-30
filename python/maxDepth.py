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

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),
                       self.maxDepth(root.right))

    def test(self):
        print(self.maxDepth(self.root))


# root = [3,9,20,null,null,15,7]
n1 = TreeNode(3)
n2 = n1.left = TreeNode(9)
n3 = n1.right = TreeNode(20)
n4 = n2.left = TreeNode(None)
n5 = n2.right = TreeNode(None)
n6 = n3.left = TreeNode(15)
n7 = n3.right = TreeNode(7)

bt = Solution(n1)
