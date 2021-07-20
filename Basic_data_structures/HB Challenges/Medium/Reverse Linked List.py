# https://fellowship.hackbrightacademy.com/materials/challenges/rev-linked-list/index.html#rev-linked-list

# Write a function that takes the head node of a linked list and returns the head of a new linked list, where the nodes are in the reverse order.

# For example, given this list:

# return this list:

# We’ve provided a Node class with a helper method for printing that node and all following nodes (this is used by our tests and is useful for debugging):
# reversell.py

# We’ve also provided the start of a reverse_linked_list function:
# reversell.py

# It should work like this:

# >>> ll = Node(1, Node(2, Node(3)))
# >>> new_ll = reverse_linked_list(ll)
# >>> new_ll.as_string()
# '321'

# Complete this function.

class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string.

        >>> Node(3).as_string()
        '3'

        >>> Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)

def reverse_linked_list(head):
    """Given LL head node, return head node of new, reversed linked list.

    >>> ll = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list(ll).as_string()
    '321'
    """
    out_head = None
    n = head
    
    while n:
            out_head = Node(n.data, out_head)
            n = n.next
    return out_head



