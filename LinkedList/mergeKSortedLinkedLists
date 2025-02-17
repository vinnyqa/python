# You are given an array of k linked lists lists, where each list is sorted in ascending order.
# Return the sorted linked list that is the result of merging all of the individual linked lists.
# ITERATION
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:    
    def mergeKLists(self, lists: list[ListNode]) -> [ListNode]: # type: ignore
        res = ListNode(0)
        cur = res
        
        while True:
            minNode = -1
            for i in range(len(lists)):
                if not lists[i]: ## If current list is processed
                    continue
                if minNode == -1 or lists[minNode].val > lists[i].val: ## If min node is not set or # current head has smaller value.
                    minNode = i
            
            if minNode == -1:
                break
            #Merge K Sorted Lists
            cur.next = lists[minNode]
            lists[minNode] = lists[minNode].next
            cur = cur.next

        return res.next

lists=[[1,2,4],[1,3,5],[3,6]]
output = [1,1,2,3,3,4,5,6]
# Time : O(n*k), Space : O(1) where k=total num of lists, n = total num of nodes across k lists