# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head =ListNode(0)
        cur = head
        carry = 0
        while l1 or l2:
            
            list1 = l1.val if l1 else 0
            list2 = l2.val if l2 else 0

            sums = (carry+list1+list2)%10
            carry = (carry+list1+list2)//10

            cur.next = ListNode(sums)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            cur.next = ListNode(carry)

        return head.next




