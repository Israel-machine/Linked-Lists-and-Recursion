from linked_list import LinkedList

if __name__ == "__main__":
    ll = LinkedList()

    # Create the list: 30 -> 10 -> 20 -> 50
    ll.insert_at_front(10)
    ll.insert_at_front(30)
    ll.insert_at_end(20)
    ll.insert_at_end(50)
    
    print("Initial Linked List:")
    ll.display() 
    # Expected: 30 -> 10 -> 20 -> 50 -> None

    # Fix: Use recursive_sum() instead of get_sum()
    total_sum = ll.recursive_sum()
    print(f"\nRecursive Sum of all nodes: {total_sum}")

    # Fix: Use recursive_search() instead of search()
    target = 20
    found = ll.recursive_search(target)
    print(f"Searching for {target}: {'Found!' if found else 'Not Found'}")

    target_missing = 99
    found_missing = ll.recursive_search(target_missing)
    print(f"Searching for {target_missing}: {'Found!' if found_missing else 'Not Found'}")

    # Fix: Use recursive_reverse() instead of reverse()
    print("\nReversing the list...")
    ll.recursive_reverse()
    
    print("Reversed Linked List:")
    ll.display()