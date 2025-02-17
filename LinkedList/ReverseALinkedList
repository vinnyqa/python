# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            temp = curr.next #Temp Variable to store curr.next value before its lost
            curr.next = prev #Assign prev to curr.next
            prev = curr #Assign curr to prev
            curr = temp #Assign temp to curr
        return prev #Return prev

head=[0,1,2,3]
output = [3,2,1,0]
# Time : O(n), Space : O(1)