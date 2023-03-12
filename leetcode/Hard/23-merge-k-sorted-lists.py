class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = curr = ListNode()
        values = []
        for l in lists:
            while l:
                values.append(l.val)
                l = l.next
        
        for val in sorted(values):
            curr.next = ListNode(val)
            curr = curr.next

        return head.next