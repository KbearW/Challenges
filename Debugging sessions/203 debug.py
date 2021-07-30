class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(self, head: ListNode, key: int) -> ListNode:
    dummy = ListNode(next = head)
    curr = head
    prev = dummy
    
    while curr:
        if curr.val == key:
            # print('yes')
            prev.next = curr.next

        else:
#                 Advance prev to next position
            prev = curr
            # prev.next = curr.next
            # print(f'prev: {prev}')
        # print(f'curr:{curr}')
        # print(f'prev:{prev}')
        curr = curr.next

    return head
        
print(removeElements([7,7,7,7],7))