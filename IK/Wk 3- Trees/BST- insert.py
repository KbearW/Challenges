# Runtime: O(height) --> O(log n)
    #        44
    #      /     \
    #     17     88
    #     /\     /  \
    #    8 32  65   97
    #      /   /\   /
    #     28  54 82 93
    #      \      /
    #      29    76
    #             \
    #             80

# Insert = 68

class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def insert(root, key):
    newnode = TreeNode(key)
    if root is None:
        return newnode
    prev = None
    curr = root
    while curr is not None:
        if key == curr.key:
            print('Key already exists')
        elif key < curr.key:
            prev = curr
            curr = curr.left
        else:
            prev = curr
            curr = curr.right
    if key < prev.key:
        prev.left = newnode
    else:
        prev.right = newnode
    return root