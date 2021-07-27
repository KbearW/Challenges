# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:

# Input: root = [1,null,2]
# Output: 2

# Example 3:

# Input: root = []
# Output: 0

# Example 4:

# Input: root = [0]
# Output: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        # Try #1
        if root is None:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

#     Tips:
#         Address the edge case first
#         Split the node to left and right, find the max +1 for the current layer
#     Note:
#   binary tree, need recursion, starts from bottom up and split the root to .left and .right for each layer
#             sudo:
# count = 0
# setup the base case so it will run--> 
# while root: (aka when root != None)
    # base case
    # if root.left == None and root.right == None:
        # count += 1 #when ropot = [0]
#     elif root.left or root.right:
#        count += max(maxDepth(root.left), maxDepth(root.right)) +1
    
# return count (this is the edge case for the while loop)