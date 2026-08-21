# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        start, curr = ListNode(0), head
        start.next = head

        while curr and curr.next:
            if curr.val <= curr.next.val:
                curr = curr.next
            else:
                prev = start
                while prev.next.val < curr.next.val:
                    prev = prev.next

                to_move = curr.next
                curr.next = to_move.next
                to_move.next = prev.next
                prev.next = to_move

        return start.next