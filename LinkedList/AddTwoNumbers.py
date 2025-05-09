# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy #Assign dummy to Left

        carry = 0
        while l1 or l2 or carry: #Iterate until l1/l2 has digits
            v1 = l1.val if l1 else 0 #v1 is digit from list1 or else set it to 0
            v2 = l2.val if l2 else 0 #v2 is digit from list2 or else set it to 0

            # new digit
            val = v1 + v2 + carry #Compute new digit(sum) including carry
            carry = val // 10 #Calculate carry
            val = val % 10 #Ones place
            cur.next = ListNode(val) #Insert New ListNode with value just computed

            # update ptrs
            cur = cur.next #Current is assigned to next pointer
            l1 = l1.next if l1 else None #L1 is assigned to l1.next
            l2 = l2.next if l2 else None #L2 is assigned to l2.next

        return dummy.next #
    
l1=[1,2,3]
l2=[4,5,6]
Output = [5,7,9]    
# Time : O(m+n), Space : O(1)