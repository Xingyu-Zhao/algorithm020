class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNode_handle:
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        # add a new node pointed to previous node
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

from sklearn.model_selection import train_test_split
ListNode_1 = ListNode_handle()
l1 = ListNode()
l1_list = [1,8,3]
for i in l1_list:
    ListNode_1.add(i)

print(ListNode_1)

m = 0

nums2 = [1,3,4]
n = 1
solu = Solution()
print(solu.mergeTwoLists(l1 = nums1, l2 = nums2))