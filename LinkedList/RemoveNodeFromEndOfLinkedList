# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        left = dummy #Assign dummy to Left
        right = head

        while n > 0 and right: #Shift Right by 1 and Decrement n by 1
            right = right.next
            n -= 1

        while right: #Until right is null or end of list
            left = left.next 
            right = right.next

        #Delete Node
        left.next = left.next.next
        return dummy.next #
    
head=[1,2,3,4]
n=2
Output = [1,2,4]
# Time : O(n), Space : O(1)