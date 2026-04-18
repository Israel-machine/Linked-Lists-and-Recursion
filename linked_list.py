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

# ---- RECURSIVE METHODS (Helpers) ----
    def get_sum(self):
        return self._recursive_sum(self.head)

    def _recursive_sum(self, node):
        if node is None:
            return 0
        return node.data + self._recursive_sum(node.next)
##=====
    def search(self, target):
        """Standard search method."""
        return self._recursive_search(self.head, target)

    def recursive_search(self, target):
        """
        Alias for the automated tests. 
        Calls the same logic but matches the expected test name.
        """
        return self.search(target)

    def _recursive_search(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        return self._recursive_search(node.next, target)

##=====

    def reverse(self):
        self.head = self._recursive_reverse(self.head, None)

    def _recursive_reverse(self, current, prev):
        if current is None:
            return prev
        next_node = current.next
        current.next = prev  
        return self._recursive_reverse(next_node, current)

    def display(self):
        elems = []
        curr = self.head
        while curr:
            elems.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elems) + " -> None")

 # --- MANUAL TESTING ---
    if __name__ == "__main__":
        ll = LinkedList()
        ll.insert_at_front(10)
        ll.insert_at_front(20)
        ll.insert_at_end(5)
        
        print("List Structure:")
        ll.display() # Should show 20 -> 10 -> 5
        
        print(f"Recursive Sum: {ll.get_sum()}") # Should be 35
        print(f"Search for 10: {ll.search(10)}") # Should be True
        print(f"Search for 100: {ll.search(100)}") # Should be False
        
        print("Reversing list...")
        ll.reverse()
        ll.display() # Should show 5 -> 10 -> 20
