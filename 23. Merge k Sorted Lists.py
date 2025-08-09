# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        try:
            min_heap = []
            for idx, node in enumerate(lists):
                if node:
                    heapq.heappush(min_heap, (node.val, idx, node))
            dummy = ListNode(0)
            curr = dummy
            while min_heap:
                val, idx, node = heapq.heappop(min_heap)
                curr.next = node
                curr = curr.next
                if node.next:
                    heapq.heappush(min_heap, (node.next.val, idx, node.next))
            return dummy.next
        except Exception as e:
            print(f"Error occurred: {e}")
            return None
