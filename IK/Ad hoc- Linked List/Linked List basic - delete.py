class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# find the previous node of the node to be deleted
# change the next of the prev node
# free memory for the node to be deleted
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    # given a reference to the head of a list and a key, 
    # delete the first occurrence of key in linked list
    def deleteNode(self,key):
        temp = self.head
        if (temp is not None):
            