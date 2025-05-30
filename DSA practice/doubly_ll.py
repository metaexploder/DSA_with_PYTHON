class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            last = curr
            curr = curr.next
        print("None")

    def display_backward(self):
        curr = self.head
        if not curr:
            print("None")
            return

        # Go to the last node
        while curr.next:
            curr = curr.next

        # Traverse backward
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.prev
        print("None")

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def prepend(self, data):
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):
        if index == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        curr = self.head
        i = 0
        while curr and i < index - 1:
            curr = curr.next
            i += 1

        if not curr:
            print("Index out of range")
            return

        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node

    def delete_key(self, key):
        curr = self.head

        while curr:
            if curr.data == key:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                return
            curr = curr.next

    def delete_all_keys(self, key):
        curr = self.head
        while curr:
            next_node = curr.next
            if curr.data == key:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
            curr = next_node

    def delete_at_index(self, index):
        if not self.head:
            return
        curr = self.head
        i = 0
        if index == 0:
            self.head = curr.next
            if self.head:
                self.head.prev = None
            return
        while curr and i < index:
            curr = curr.next
            i += 1
        if curr:
            if curr.prev:
                curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev

    def search(self, key):
        curr = self.head
        i = 0
        found = False
        while curr:
            if curr.data == key:
                print("Found at index:", i)
                found = True
            curr = curr.next
            i += 1
        if not found:
            print("Not found.")

    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        print("Length:", count)

# Example usage:
dll = DoublyLinkedList()

for val in [1, 2, 3, 4, 2, 5]:
    dll.append(val)

dll.display_forward()      # 1 <-> 2 <-> 3 <-> 4 <-> 2 <-> 5 <-> None
dll.display_backward()     # 5 <-> 2 <-> 4 <-> 3 <-> 2 <-> 1 <-> None

dll.insert_at_index(2, 99) # Insert 99 at index 2
dll.display_forward()

dll.delete_key(2)          # Delete first 2
dll.display_forward()

dll.delete_all_keys(2)     # Delete all 2s
dll.display_forward()

dll.delete_at_index(3)     # Delete node at index 3
dll.display_forward()

dll.search(99)             # Search for 99
dll.length()               # Length
