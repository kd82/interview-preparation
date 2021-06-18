class Node:
    def __init__(self, x: int):
        self.val = int(x)
        self.next = None
        self.random = None
class Solution:
    def copyRandomList(head: 'Node') -> 'Node': #recursive implementation which makes sense to me
        node_dict = {}
        def copy(head):
            if not head:
                return None
            if head in node_dict:
                return node_dict[head]
            new_head = Node(head.val)            
            new_head.next = copy(head.next)
            new_head.random = copy(head.random)
            return new_head
        return copy(head)
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        node_dict = {}
        node = head
        while node:
            if node not in node_dict:
                node_dict[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            if node.random != None:
                node_dict[node].random = node_dict[node.random]
            if node.next != None:
                node_dict[node].next = node_dict[node.next]
            node = node.next
        return node_dict[head]