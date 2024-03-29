# https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:

# Input: head = [1,2]
# Output: [2,1]

# Example 3:

# Input: head = []
# Output: []

 

# Constraints:

#     The number of nodes in the list is the range [0, 5000].
#     -5000 <= Node.val <= 5000

 

# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, data=0, next=None):
#         self.data = data
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        self.head = None
        prev = None
        
        while head != None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        
        return prev

# Tips:
# Need to setup three variables and understand what does head.next do.
# 1.) head or current, 2.) prev, 3.) next_node
# draw it out, think about it. 
# for the while loop--> the last statement will some what like this.... head = next_head