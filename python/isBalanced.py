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

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depthFirst(node):
            if not node:
                return [True, 0]
            l = depthFirst(node.left)
            r = depthFirst(node.right)
            subtree = l[0] and r[0]
            heights = abs(l[1] - r[1]) <= 1
            return [subtree and heights, 1 + max(l[1], r[1])]
        return depthFirst(root)[0]

    def test(self):
        print(self.isBalanced(self.root))


# [1,2,2,3,3,null,null,4,4]
n1 = TreeNode(1)
n2 = n1.left = TreeNode(2)
n3 = n1.right = TreeNode(2)
n4 = n2.left = TreeNode(3)
n5 = n2.right = TreeNode(3)
# n6 = n3.left = TreeNode(None)
# n7 = n3.right = TreeNode(None)
n8 = n4.left = TreeNode(4)
n9 = n4.right = TreeNode(4)

bt = Solution(n1)
