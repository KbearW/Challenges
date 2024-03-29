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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # This method is looking at curr.next--> doesn't need to create new var: prev  

        # basic edge cases: 
        # (1) when head.node == key, 
        # (2) when middle node == key,
        # (3) when last node == key

        # To simplfy edge cases:
        # --> create a dummy node to put edge #1 and #2 together
        # --> look at it from curr.next and by not using prev... edge #3 will be taken care of

        dummy = ListNode(None)
        dummy.next = head
        
        curr = dummy
        # keep running if curr.next is not none
        while curr.next:
            
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return dummy.next

# Q: What happen to when the last node matches key?
# In that case, node.next is none and will bypass the while loop

# Answer: This method looks at .next and not curr, so when last node matches key, curr.next would have 
# already caught it and curr.next would have already been updated.

# Explain:
# Before writing any code, it's good to make a list of edge cases that we need to consider. This is so that we can be certain that we're not overlooking anything while coming up with our algorithm, and that we're testing all special cases when we're ready to test. These are the edge cases that I came up with.

#     The linked list is empty, i.e. the head node is None.
#     Multiple nodes with the target value in a row.
#     The head node has the target value.
#     The head node, and any number of nodes immediately after it have the target value.
#     All of the nodes have the target value.
#     The last node has the target value.

# So with that, this is the algorithm I came up with.

# In order to save the need to treat the "head" as special, the algorithm uses a "dummy" head. This simplifies the code greatly, particularly in the case of needing to remove the head AND some of the nodes immediately after it.

# Then, we keep track of the current node we're up to, and look ahead to its next node, as long as it exists. If current_node.next does need removing, then we simply replace it with current_node.next.next. We know this is always "safe", because current_node.next is definitely not None (the loop condition ensures that), so we can safely access its next.

# Otherwise, we know that current_node.next should be kept, and so we move current_node on to be current_node.next.

# The loop condition only needs to check that current_node.next != None. The reason it does not need to check that current_node != None is because this is an impossible state to reach. Think about it this way: The ONLY case that we ever do current_node = current_node.next in is immediately after the loop has already confirmed that current_node.next is not None.

# The algorithm requires O(1) extra space and takes O(n) time.