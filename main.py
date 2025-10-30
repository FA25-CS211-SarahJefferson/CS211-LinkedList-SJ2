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
    ### saving it to the head each time because it is returning the previous data to head each time

    # Element insertion at the beginning
    head = ll.insert_at_beginning(100)
    head = ll.insert_at_beginning(200)
    ll.display(head)
    ### add display at the end of most of functions

    # Get the length of the ll
    ll.len(head)
    ll.display(head)

    # Search for an element in the ll

    # Search for an element that does not exist in the ll
        # Think about using conditional logic to handle this case(will be the same as above just adding if 
        # else and using comparisions)

    # Delete an element in the ll
    head = ll.del(50)
    ll.display(head)

    # Get final length of the ll (very similar to line 19)


if __name__ == "__main__":
    main()