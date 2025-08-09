# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        def reverse(start, end):
            prev = end
            curr = start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        length = getLength(head)
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        while length >= k:
            start = prev_group.next
            end = start
            for _ in range(k):
                end = end.next
            new_head = reverse(start, end)
            prev_group.next = new_head
            prev_group = start
            length -= k
        return dummy.next
