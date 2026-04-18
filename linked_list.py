class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
            """Traverses to the end to add a new node."""
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                return
            
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

