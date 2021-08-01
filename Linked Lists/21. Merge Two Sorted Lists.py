# https://leetcode.com/problems/merge-two-sorted-lists/

# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

# Example 1:

# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: l1 = [], l2 = []
# Output: []

# Example 3:

# Input: l1 = [], l2 = [0]
# Output: [0]


# iteratively
def mergeTwoLists1(self, l1, l2):
#   Pseudo code:
#       setup a dummy node and curr--> look at curr.next only
#       dummy = curr = ListNode(None)
#       while l1 and l2:
#           edge case #1: if l1.val < l2.val --> curr.next --> l1, advance l1
#           edge case #2: else: curr.next --> l2, advance l2
#       regardless of edge cases: move curr to next --> curr = curr.next
#       return dummy.next

        dummy = curr = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
#               Advance curr to curr.next
            curr = curr.next
#       advance curr.next to l1 or l2 --> if any one of them is true. This doesn't matter bc curr.next will be reset in both edge cases
        curr.next = l1 or l2
        return dummy.next
    
# recursively    
def mergeTwoLists2(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
        
# in-place, iteratively        
def mergeTwoLists(self, l1, l2):
    if None in (l1, l2):
        return l1 or l2
    dummy = cur = ListNode(0)
    dummy.next = l1
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            nxt = cur.next
            cur.next = l2
            tmp = l2.next
            l2.next = nxt
            l2 = tmp
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next