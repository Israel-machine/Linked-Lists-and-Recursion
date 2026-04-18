from linked_list import LinkedList

if __name__ == "__main__":

    # TODO: 1) Create a LinkedList instance
    ll = LinkedList()

    # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
    # Let's create the list: 30 -> 10 -> 20 -> 50
    ll.insert_at_front(10)
    ll.insert_at_front(30)
    ll.insert_at_end(20)
    ll.insert_at_end(50)
    
    # TODO: 3) Display the list to verify insertion
    print("Initial Linked List:")
    ll.display() 
    # Expected Output: 30 -> 10 -> 20 -> 50 -> None

    # TODO: 4) Call recursive_sum and print the result
    total_sum = ll.get_sum()
    print(f"\nRecursive Sum of all nodes: {total_sum}")
    # Expected Output: 110

    # TODO: 5) Call recursive_search with a target and print result
    target = 20
    found = ll.search(target)
    print(f"Searching for {target}: {'Found!' if found else 'Not Found'}")

    target_missing = 99
    found_missing = ll.search(target_missing)
    print(f"Searching for {target_missing}: {'Found!' if found_missing else 'Not Found'}")

    # TODO: 6) Call recursive_reverse, then display the reversed list
    print("\nReversing the list...")
    ll.reverse()
    
    print("Reversed Linked List:")
    ll.display()
    # Expected Output: 50 -> 20 -> 10 -> 30 -> None