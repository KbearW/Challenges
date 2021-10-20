# BFS
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
            node = q.popleft()
            if node.left_ptr is not None:
                q.append(node.left_ptr)
            if node.right_ptr is not None:
                q.append(node.right_ptr)
            temp.append(node.label)
        res.append(temp)
    return res
    