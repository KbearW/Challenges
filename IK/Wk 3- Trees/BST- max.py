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

def max(root):
    if root is  None:
        return None
    curr = root
    # we can use a prev pointer so the final return statement would work but we can simipfy it with 
    # checking curr.left
    while curr.right is not None:
        curr = curr.right
    return curr.key
