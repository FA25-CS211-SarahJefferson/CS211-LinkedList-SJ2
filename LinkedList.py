"""
Linked List implementation using functions (no OOP).

This module provides a functional approach to implementing a linked list
data structure in Python. Instead of using classes and objects, this
implementation uses:

1. Dictionaries to represent nodes:
   - Each node is a dict with 'data' and 'next' keys
   - 'data' stores the actual value
   - 'next' stores a reference to the next node (or None if it's the last node)

2. Functions to manipulate the linked list:
   - Functions take the head of the list as a parameter
   - Functions return the (possibly new) head of the list
   - No global state or mutable objects are used

This approach demonstrates that linked lists can be implemented without
Object-Oriented Programming, using pure functional programming concepts.

Key Concepts:
-------------
- A linked list is a linear data structure where elements are not stored
  in contiguous memory locations
- Each element (node) contains data and a reference (link) to the next node
- The first node is called the "head"
- The last node's 'next' pointer is None, indicating the end of the list

Advantages of Linked Lists:
----------------------------
- Dynamic size (can grow/shrink easily)
- Easy insertion/deletion at the beginning (O(1) time)
- No memory waste from pre-allocated space

Disadvantages:
--------------
- No random access (must traverse from head)
- Extra memory for storing references
- Not cache-friendly due to non-contiguous memory

Available Functions:
--------------------
- create_node(data): Create a new node
- insert_at_beginning(head, data): Insert at start - O(1)
- insert_at_end(head, data): Insert at end - O(n)
- delete_node(head, data): Delete first matching node - O(n)
- search(head, data): Find position of data - O(n)
- display(head): Print the list visually
- get_length(head): Count total nodes - O(n)

Usage Example:
--------------
import linked_list as ll

head = None
head = ll.insert_at_end(head, 10)
head = ll.insert_at_end(head, 20)
ll.display(head)  # Output: 10 -> 20 -> None
"""


"""
    Create a new node for the linked list.
    
    A node is represented as a dictionary with two keys:
    - 'data': stores the actual value/information in the node
    - 'next': stores a reference (pointer) to the next node in the list
    
    When a node is first created, its 'next' pointer is set to None,
    indicating it doesn't point to any other node yet.
    
    Parameters:
    data : any type
        The value to be stored in the node. Can be an integer, string,
        or any other data type.
    
    Returns:
    dict
        A dictionary representing a node with keys 'data' and 'next'.
        The 'next' key is initialized to None.
    
    Example:
    node = create_node(10)
    # Returns: {'data': 10, 'next': None}
    """
def create_node(data):
    return {'data': data, 'next': None}


"""
    Insert a new node at the beginning (start) of the linked list.
    
    This function creates a new node with the given data and makes it the
    new head (first node) of the list. The previous head becomes the second
    node in the list.
    
    How it works:
    1. Creates a new node using create_node(data)
    2. Sets the new node's 'next' pointer to point to the current head
    3. Returns the new node as the new head of the list
    
    Time Complexity: O(1) - constant time, very fast regardless of list size
    
    Parameters:
    head : dict or None
        The current head (first node) of the linked list. If the list is
        empty, this will be None.
    data : any type
        The value to be stored in the new node.
    
    Returns:
    dict
        The new head of the linked list (the newly created node).
    
    Example:
    head = None
    head = insert_at_beginning(head, 10)  # List: 10 -> None
    head = insert_at_beginning(head, 5)   # List: 5 -> 10 -> None
    """
def insert_at_beginning(head, data):
    new_node = create_node(data)
    new_node['next'] = head
    return new_node


"""
    Insert a new node at the end (tail) of the linked list.
    
    This function creates a new node and adds it to the end of the list.
    It must traverse the entire list to find the last node before inserting.
    
    How it works:
    1. Creates a new node using create_node(data)
    2. If the list is empty (head is None), returns the new node as head
    3. Otherwise, traverses the list from head to find the last node
       (the node whose 'next' pointer is None)
    4. Sets the last node's 'next' pointer to the new node
    5. Returns the original head (unchanged)
    
    Time Complexity: O(n) - linear time, where n is the number of nodes.
                     Must traverse entire list to reach the end.
    
    Parameters:
    head : dict or None
        The current head (first node) of the linked list. If the list is
        empty, this will be None.
    data : any type
        The value to be stored in the new node.
    
    Returns:
    dict
        The head of the linked list (unchanged if list was not empty,
        or the new node if list was empty).
    
    Example:
    head = None
    head = insert_at_end(head, 10)  # List: 10 -> None
    head = insert_at_end(head, 20)  # List: 10 -> 20 -> None
    head = insert_at_end(head, 30)  # List: 10 -> 20 -> 30 -> None
    """
def insert_at_end(head, data):
    new_node = create_node(data)
    
    if head is None:
        return new_node
    
    current = head
    while current['next'] is not None:
        current = current['next']
    
    current['next'] = new_node
    return head


    """
    Delete the first node that contains the specified data value.
    
    This function searches for the first node with the given data and removes
    it from the linked list by adjusting the pointers. Only the first matching
    node is deleted; if there are multiple nodes with the same data, only the
    first one encountered is removed.
    
    How it works:
    1. If the list is empty (head is None), returns None
    2. If the head node contains the data to delete:
       - Returns the second node (head['next']) as the new head
       - This effectively removes the first node from the list
    3. Otherwise, traverses the list to find a node whose next node contains
       the data to delete
    4. When found, bypasses that node by setting current['next'] to
       current['next']['next'], effectively removing it from the chain
    5. Returns the original head
    
    Time Complexity: O(n) - linear time, where n is the number of nodes.
                     May need to traverse the entire list in worst case.
    
    Parameters:
    head : dict or None
        The current head (first node) of the linked list.
    data : any type
        The value to search for and delete from the list.
    
    Returns:
    dict or None
        The head of the linked list after deletion. Returns None if the
        list becomes empty, or the new head if the first node was deleted.
    
    Example:
    # List: 5 -> 10 -> 20 -> 30 -> None
    head = delete_node(head, 20)   # List: 5 -> 10 -> 30 -> None
    head = delete_node(head, 5)    # List: 10 -> 30 -> None
    head = delete_node(head, 100)  # List: 10 -> 30 -> None (no change)
    """
def delete_node(head, data):
    if head is None:
        return None
    
    # If head node contains the data
    if head['data'] == data:
        return head['next']
    
    current = head
    while current['next'] is not None:
        if current['next']['data'] == data:
            current['next'] = current['next']['next']
            return head
        current = current['next']
    
    return head


 """
    Search for a node containing the specified data value.
    
    This function traverses the linked list from the beginning and searches
    for the first node that contains the specified data. It returns the
    position (index) of the node if found, or -1 if not found.
    
    How it works:
    1. Starts at the head node with position counter set to 0
    2. Checks if the current node's data matches the search data
    3. If match is found, returns the current position
    4. If no match, moves to the next node and increments position
    5. Continues until the end of the list is reached
    6. Returns -1 if the data is not found in any node
    
    Time Complexity: O(n) - linear time, where n is the number of nodes.
                     May need to check every node in worst case.
    
    Parameters:
    head : dict or None
        The current head (first node) of the linked list.
    data : any type
        The value to search for in the linked list.
    
    Returns:
    int
        The position (0-based index) of the first node containing the data.
        Returns -1 if the data is not found in the list.
        Position 0 means the head node, position 1 means the second node, etc.
    
    Example:
    # List: 5 -> 10 -> 20 -> 30 -> None
    position = search(head, 20)   # Returns: 2
    position = search(head, 5)    # Returns: 0
    position = search(head, 100)  # Returns: -1 (not found)
    """
def search(head, data):
    current = head
    position = 0
    
    while current is not None:
        if current['data'] == data:
            return position
        current = current['next']
        position += 1
    
    return -1


def display(head):
    """
    Display all nodes in the linked list in a visual format.
    
    This function traverses the entire linked list and prints all the data
    values in a visual representation showing the connections between nodes.
    The output format is: data1 -> data2 -> data3 -> None
    
    This visualization helps understand the structure of the linked list:
    - Each data value is shown
    - Arrows (->) show the direction of links between nodes
    - 'None' at the end indicates the end of the list
    
    How it works:
    1. If the list is empty (head is None), prints "List is empty"
    2. Otherwise, starts at the head and traverses through each node
    3. Collects each node's data (converted to string) in a list
    4. Joins all data values with " -> " separator
    5. Adds " -> None" at the end to show the list termination
    6. Prints the complete visual representation
    
    Time Complexity: O(n) - linear time, where n is the number of nodes.
                     Must visit every node to display all values.
    
    Parameters:
    head : dict or None
        The current head (first node) of the linked list.
    
    Returns:
    None
        This function doesn't return anything; it prints to console.
    
    Example:
    # If list contains: 5 -> 10 -> 20 -> None
    display(head)
    # Output: 5 -> 10 -> 20 -> None
    
    # If list is empty:
    display(None)
    # Output: List is empty
    """
    if head is None:
        print("List is empty")
        return
    
    current = head
    elements = []
    
    while current is not None:
        elements.append(str(current['data']))
        current = current['next']
    
    print(" -> ".join(elements) + " -> None")


    """
    Get the total number of nodes in the linked list.
    
    This function counts how many nodes exist in the linked list by
    traversing from the head to the end and incrementing a counter
    for each node encountered.
    
    How it works:
    1. Initializes a count variable to 0
    2. Starts at the head node
    3. Traverses through each node in the list
    4. For each node visited, increments the count by 1
    5. Continues until reaching the end (when current becomes None)
    6. Returns the total count
    
    Time Complexity: O(n) - linear time, where n is the number of nodes.
                     Must visit every node to count them all.
    
    Parameters:
    head : dict or None
        The current head (first node) of the linked list.
    
    Returns:
    int
        The total number of nodes in the linked list.
        Returns 0 if the list is empty (head is None).
    
    Example:
    # List: 5 -> 10 -> 20 -> None
    length = get_length(head)  # Returns: 3
    
    # Empty list:
    length = get_length(None)  # Returns: 0
    """
def get_length(head):
    count = 0
    current = head
    
    while current is not None:
        count += 1
        current = current['next']
    
    return count