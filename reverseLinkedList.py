from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head):
        self.head = ListNode(head)
        self.test()

    def swap(self, curr, after):
        if after.next:
            self.swap(curr.next, after.next)
        else:
            self.new = after
        after.next = curr

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        self.new = None
        self.swap(head, head.next)
        head.next = None
        return self.new

    def test(self):
        print(self.reverseList(self.head))


heads = [[1, 2, 3, 4, 5], {1, 2}, []]
for head in heads:
    s = Solution(head)
