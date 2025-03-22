# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
# The new list should be made up of nodes from list1 and list2.

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, head: ListNode) -> ListNode:
        dummy = ListNode() #Create a dummynode that acts as the head of the merged list.
        tail = dummy #Use a pointer (tail) to keep track of the current node in the merged list.

        while l1 and l2:
            if l1.val < l2.val: #Compare the values of the nodes in list1 andlist2.
                tail.next = l1 #Append the smaller value to the merged list and move the respective pointer (list1orlist2) forward.
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next #Move forward the current pointer

        if l1:
            tail.next = l1 #If one of the lists is exhausted, append the remaining nodes of the other list to the merged list.
        elif l2:
            tail.next = l2

        return dummy.next #The merged list starts from dummy.next.

list1=[1,2,4]
list2=[1,3,5]
output = [1,1,2,3,4,5]
# Time : O(n+m), Space : O(1)
