# # https://fellowship.hackbrightacademy.com/materials/challenges/remove-ll-node/index.html#remove-ll-node

# You will have a linked list defined using a simple Node class:
# removellnode.py

# class Node(object):
#     """Class in a linked list."""

#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

#     def as_string(self):
#         """Represent data for this node and it's successors as a string.

#         >>> Node(3).as_string()
#         '3'

#         >>> Node(3, Node(2, Node(1))).as_string()
#         '321'
#         """

#         out = []
#         n = self

#         while n:
#             out.append(str(n.data))
#             n = n.next

#         return "".join(out)

# It will have a data and next attribute. There is no LinkedList class—just individual Node objects which point to each other.

# For a list like:

# You could build this like:

# >>> four_node = Node(4)
# >>> three_node = Node(3, four_node)
# >>> two_node = Node(2, three_node)
# >>> one_node = Node(1, two_node)

# Or, more tersely:

# >>> one_node = Node(1, Node(2, Node(3, Node(4))))

# We want a function that will delete a node from the series, so that everything moves over by one.

# For example, if we deleted the “3” node, above, we’d get:

# Your function should be able to delete the first node or any node in the middle. It will not be used to delete the tail node.

# We’ve provided a file, removellnode.py, with a stub of a function, remove_node:
# removellnode.py

def remove_node(node):
    # ***DO NOT HAVE ACCESS TO OTHER NODES!!! HENCE: DELETE the next node!
    """Given a node in a linked list, remove it.

    Remove this node from a linked list. Note that we do not have access to
    any other nodes of the linked list, like the head or the tail.

    Does not return anything; changes list in place.
    """
    while node.next:
        node.data = node.next.data
        node.next = node.next.next
# However, this is unimplemented. Write it.
