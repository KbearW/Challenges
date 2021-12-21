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

# find the min

class NodeTree():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
def min(root):
    if root is  None:
        return None
    curr = root
    while curr is not None:
        curr = curr.left
    return curr.key
