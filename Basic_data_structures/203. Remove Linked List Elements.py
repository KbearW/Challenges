# https://leetcode.com/problems/remove-linked-list-elements/


# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:

# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:

# Input: head = [], val = 1
# Output: []

# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []

# #Note:
# Add a dummy node to the beginning and use the normal variable as before to traverse the list.

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        curr = head
        prev = dummy
        # prev.next = head
        
        while curr:
            nextNode = curr.next

            if curr.val == val:
                prev.next = nextNode

            else:
                prev = curr
            curr = nextNode
        return dummy.next