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

    # given a reference to the head of a list and a key, 
    # delete the first occurrence of key in linked list
    def deleteNode(self,key):
        temp = self.head
        # if head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

    # Search for the key to be deleted, keep track of the 
    # prev node as we need to change prev.next
        while (temp is not None):
            if temp.data == key:                break
            prev = temp
            temp = temp.next

        # if key was not present in the LL
        if (temp == None):
            return

        # Unlink the node from LL
        prev.next = temp.next

        temp = None