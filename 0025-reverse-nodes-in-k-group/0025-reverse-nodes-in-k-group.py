class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        def get_kth(node, k):
            while node and k > 0:
                node = node.next
                k -= 1
            return node

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp

        return dummy.next
