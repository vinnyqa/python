# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
# There is a cycle in a linked list if at least one node in the list that can be visited again by following the next pointer.
# Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head #Slow & Fast will be at same position

        while fast and fast.next: #Make sure fast and fast.next is NOT null
            slow = slow.next #Shift slow by 1
            fast = fast.next.next #Shift fast by 2
            if slow == fast:
                return True
        return False

head=[1,2,3,4]
index=1
#output = true
# Time : O(n), Space : O(1)