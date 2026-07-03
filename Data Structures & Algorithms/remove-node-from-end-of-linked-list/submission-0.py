# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # fast 先走 n 步
        for _ in range(n):
            fast = fast.next

        # slow 和 fast 一起走
        # 直到 fast 到最后一个节点
        while fast.next:
            slow = slow.next
            fast = fast.next

        # 删除 slow 后面的节点
        slow.next = slow.next.next

        return dummy.next