"""
File Name: main.py
Project Name: Linked List Demo
Author: Sarah Jefferson
Date Created: 10/29/25
"""

import LinkedList as ll

def main():
    # Initialize empty ll
    head = None

    print("Linked List Demo")

    # Element insertion at the end
    print("Inserting elemtents at the end of the link list")
    head = ll.insert_at_end(head, 25)
    head = ll.insert_at_end(head, 50)
    head = ll.insert_at_end(head, 75)
    ll.display(head)

    # Element insertion at the beginning
    print("Inserting elemtents at the beginning of the link list")
    head = ll.insert_at_beginning(head, 100)
    head = ll.insert_at_beginning(head, 200)
    ll.display(head)

    # Get the length of the ll
    print("Getting the length of the link list")
    print("Legth of link list:", ll.get_length(head))

    # Search for an element in the ll
    print("Searching for an element in the link list.")
    print("It is in position:", ll.search(head, 50))
    
    # Search for an element that does not exist in the ll
    print("Searching for an element that does not exist in the link list.")
    result = ll.search(head, 20)
    
    if result == -1:
        print("That node is not in the link list.")
    else:
        print(f"That node is in position {result}")


    # Delete an element in the ll
    print("Deleting an element from the link list.")
    ll.delete_node(head, 100)
    ll.display(head)

    # Get final length of the ll (very similar to line 19)
    print("Getting the final length of the link list")
    print("Final length of link list:", ll.get_length(head))


if __name__ == "__main__":
    main()