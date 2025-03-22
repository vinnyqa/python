# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import Optional

class Solution:
    def reorderList(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next #Shifted by 1
            fast = fast.next.next #Shifted by 2

        second = slow.next #Beginning of 2nd Half of List
        prev = slow.next = None 
        while second:
            tmp = second.next #This is same code of Reversing Linked List
            second.next = prev
            prev = second
            second = tmp

        #Merge 2 halfs of List
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

head=[2,4,6,8]
Output=[2,8,4,6]
# Time : O(n), Space : O(1)