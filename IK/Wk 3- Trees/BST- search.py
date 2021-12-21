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

# Search = 68

class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def search(root, key):
    if root is None:
        return None
    curr = root
    while curr is not None:
        if key == curr.key:
            return curr
        elif key < curr.key:
            curr = curr.left
        else:
            curr = curr.right
    return None