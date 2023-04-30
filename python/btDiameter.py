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

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def depthFirst(root):
            nonlocal count
            if not root:
                return 0
            l = depthFirst(root.left)
            r = depthFirst(root.right)
            count = max(count, l + r)
            return max(l, r) + 1
        depthFirst(root)
        return count

    def test(self):
        print(self.diameterOfBinaryTree(self.root))


# root = [1,2,3,4,5]
n1 = TreeNode(1)
n2 = n1.left = TreeNode(2)
n3 = n1.right = TreeNode(3)
n4 = n2.left = TreeNode(4)
n5 = n2.right = TreeNode(5)

bt = Solution(n1)
