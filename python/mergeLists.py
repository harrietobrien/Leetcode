from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        res = ""
        ptr = self.head
        while ptr:
            res += str(ptr.val) + ", "
            ptr = ptr.next
        res = res.strip(", ")
        return "[{res}]".format(res=res) \
            if len(res) else "[]"


class Solution:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        self.test()

    @staticmethod
    def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode()
        tail = tmp
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2 \
            if list2 else None
        return tmp.next

    def test(self):
        merge = self.mergeTwoLists(self.list1, self.list2)
        llm = LinkedList(merge)
        print(llm.__str__())


ll1 = LinkedList()
l1_n1, l1_n2, l1_n3 = ListNode(1), ListNode(2), ListNode(3)
ll1.head = l1_n1
l1_n1.next = l1_n2
l1_n2.next = l1_n3

ll2 = LinkedList()
l2_n1, l2_n2, l2_n3 = ListNode(1), ListNode(3), ListNode(4)
ll2.head = l2_n1
l2_n1.next = l2_n2
l2_n2.next = l2_n3

test = Solution(ll1.head, ll2.head)
