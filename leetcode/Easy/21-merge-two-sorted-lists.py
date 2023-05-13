class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        head = node
        while list1 and list2:
            node.next = ListNode()
            node = node.next
            if list1.val <= list2.val:
                node.val = list1.val
                list1 = list1.next
            else:
                node.val = list2.val
                list2 = list2.next

        if list1 or list2:
            node.next = list1 if list1 else list2

        return head.next