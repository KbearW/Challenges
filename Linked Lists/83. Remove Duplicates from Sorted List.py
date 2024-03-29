# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

# Example 1:

# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while (curr != None and curr.next != None):
            if curr.next.val == curr.val:
                curr.next = curr.next.next

            else:
                curr = curr.next
#Note: IMPORTANT! return the orginal head and not the updated head!
        return head