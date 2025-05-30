# Node class to represent each element in the list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class to handle list operations
class LinkedList:
    def __init__(self):
        self.head = None

    # Make the list iterable
    def __iter__(self):
        return self._traverse()

    # Make len(ll) work
    def __len__(self):
        return self.get_length()

    # Internal generator to traverse the list
    def _traverse(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    # Get node at specific index (0-based)
    def _get_node_at(self, index):
        for i, node in enumerate(self._traverse()):
            if i == index:
                return node
        return None

    # Get length of the linked list
    def get_length(self):
        return sum(1 for _ in self._traverse())

    # Append node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        for curr in self._traverse():
            if not curr.next:
                curr.next = new_node
                return

    # Display all nodes
    def display(self):
        for node in self:
            print(node.data, end=" -> ")
        print("None")

    # Display node at a given index
    def display_with_index(self, index):
        node = self._get_node_at(index)
        if node:
            print(node.data)
        else:
            print("Index out of range.")

    # Search for key
    def search(self, key):
        found = False
        for i, node in enumerate(self):
            if node.data == key:
                print("Found at index:", i)
                found = True
        if not found:
            print("Number not found.")

    def delete_list(self):
        self.head = None # set the value of the head is to none


    # Delete first node with matching key
    def delete_key(self, key):
        curr = self.head

        if not curr:
            return

        if curr.data == key:
            self.head = curr.next
            return

        while curr.next:
            if curr.next.data == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    # Delete all nodes with matching key
    def delete_all_keys(self, key):
        while self.head and self.head.data == key:
            self.head = self.head.next

        curr = self.head
        while curr and curr.next:
            if curr.next.data == key:
                curr.next = curr.next.next
            else:
                curr = curr.next

    # Delete node at a given index
    def delete_with_index(self, index):
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        prev = self._get_node_at(index - 1)
        if prev and prev.next:
            prev.next = prev.next.next

# ----------- Test Code -----------
ll = LinkedList()

# Add elements: 1 → 3 → 1 → 4 → 5 → 6
for val in [1, 3, 1, 4, 5, 6]:
    ll.append(val)

ll.__init__()            # Output: 1 -> 3 -> 1 -> 4 -> 5 -> None
ll.display()












# -----------  MY CODE -----------

# # Node class to represent each element in the list
# class Node:
#     def __init__(self, data):
#         self.data = data      # Store the data
#         self.next = None      # Initialize next as None

# # LinkedList class to handle list operations
# class LinkedList:
#     def __init__(self):
#         self.head = None      # Start with an empty list (no head)

#     # Method to add a new node at the end of the list
#     def append(self, data):
#         new_node = Node(data)  # Create a new node with the given data

#         # If the list is empty, set new node as the head
#         if not self.head:
#             self.head = new_node
#             return

#         # Otherwise, traverse to the end of the list
#         curr = self.head
#         while curr.next:
#             curr = curr.next

#         # Set the last node's next to new node
#         curr.next = new_node

#     # Method to print the entire linked list
#     def display(self):
#         curr = self.head  # Start from the head
#         while curr:
#             print(curr.data, end=" -> ")  # Print current node's data
#             curr = curr.next              # Move to next node
#         print("None")  # End of list

#     def display_with_index(self, index):
#         curr = self.head
#         ind = 0
#         while curr:
#             if ind == index:
#                 print(curr.data)
#             curr = curr.next
#             ind += 1

#     def length(self):
#         curr = self.head
#         count = 0
#         while curr:
#             count += 1
#             curr = curr.next
#         print("Length:", count)

#     def search(self, key):
#         curr = self.head
#         i = 0
#         count = False
#         while curr:
#             if curr.data == key:
#                 print("found at:", i)
#                 count = True
#             curr = curr.next
#             i += 1
                
#         if count == False:
#             print("Number in not found..")
    
#     def delete_key(self, key):
#         curr = self.head

#         # If the list is empty
#         if not curr:
#             return

#         # If the head node holds the key
#         if curr.data == key:
#             self.head = curr.next
#             return

#         # Traverse the list to find the key
#         while curr.next:
#             if curr.next.data == key:
#                 curr.next = curr.next.next  # Delete the node by skipping it
#                 return
#             curr = curr.next


#     def delete_all_keys(self, key):
#         curr = self.head

#         # Remove key from head nodes
#         while curr and curr.data == key:
#             self.head = curr.next
#             curr = self.head

#         # Now delete remaining key nodes
#         while curr and curr.next:
#             if curr.next.data == key:
#                 curr.next = curr.next.next
#             else:
#                 curr = curr.next

#     def delete_with_index(self, index):
#         if not self.head:
#             return

#         # Delete head node
#         if index == 0:
#             self.head = self.head.next
#             return

#         curr = self.head
#         ind = 0

#         # Traverse to the node just before the one to delete
#         while curr and curr.next:
#             if ind + 1 == index:
#                 curr.next = curr.next.next
#                 return
#             curr = curr.next
#             ind += 1

    





# # Create a LinkedList object
# ll = LinkedList()

# # Add elements: 1 → 3 → 1 → 4 → 5 -> 6
# for val in [1, 3, 1, 4, 5, 6]:
#     ll.append(val)

# ll.display()
# ll.delete_with_index(5)
# ll.display()

