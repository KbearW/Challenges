# BFS, 
# Runtime: O(n)
# Space: O(n) 
import collections
def level_order_traversal(root):

    res = []   
    q = collections.deque([root])

    # Edge case
    if root is None:
        return []
        
    while len(q) != 0:
        temp = []
        numnodes = len(q)
        for _ in range(numnodes):
            # O(1) since it's limited to the # of nodes
            node = q.popleft()
            if node.left_ptr is not None:
                q.append(node.left_ptr)
            if node.right_ptr is not None:
                q.append(node.right_ptr)
            temp.append(node.label)
        res.append(temp)
    return res
    