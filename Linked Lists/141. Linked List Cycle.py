# https://leetcode.com/problems/linked-list-cycle/

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         try:
#             curr = head
#             nextNode = head.next
#             while curr != nextNode:
#                 curr = curr.next
#                 nextNode = nextNode.next.next
#             return True
#         except:
#             return False
        
# Note: ask for Bool

# if node.next is true--> true
# else, false

# Pesudo Code:
# when len(head) == 1--> no loop
# when len(head) >1 and .next is not none:
# iterate over the list to make sure every node is connected to the next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def hasCycle(head):
#  Below works:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False

hasCycle([3,2,0,-4])

# Setup two variables: slow, fast -2 steps ahead
# setup a while loop 
# advance slow and fast 
# if it doesn't match, return false
# return true