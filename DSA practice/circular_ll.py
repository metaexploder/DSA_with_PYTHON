class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        curr = self.head
        while curr.next != self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head

    def display(self):
        if not self.head:
            print("List is empty")
            return
        curr = self.head
        while True:
            print(curr.data, end=" -> ")
            curr = curr.next
            if curr == self.head:
                break
        print("(head)")

    def length(self):
        if not self.head:
            return 0
        count = 1
        curr = self.head.next
        while curr != self.head:
            count += 1
            curr = curr.next
        print("Length:", count)
        return count

    def search(self, key):
        if not self.head:
            print("List is empty")
            return

        curr = self.head
        index = 0
        found = False
        while True:
            if curr.data == key:
                print(f"Found at index {index}")
                found = True
            curr = curr.next
            index += 1
            if curr == self.head:
                break
        if not found:
            print("Not found")

    def delete_key(self, key):
        if not self.head:
            return

        curr = self.head
        prev = None

        while True:
            if curr.data == key:
                if curr == self.head:
                    # Delete head node
                    if curr.next == self.head:
                        self.head = None  # Only one node
                        return
                    else:
                        # Find last node to update its next
                        last = self.head
                        while last.next != self.head:
                            last = last.next
                        last.next = curr.next
                        self.head = curr.next
                        return
                else:
                    prev.next = curr.next
                    return
            prev = curr
            curr = curr.next
            if curr == self.head:
                break

    def delete_all_keys(self, key):
        if not self.head:
            return

        while self.head and self.head.data == key:
            self.delete_key(key)

        curr = self.head
        prev = None
        while True:
            if curr.data == key:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

            if curr == self.head:
                break

    def delete_with_index(self, index):
        if not self.head:
            return

        if index == 0:
            self.delete_key(self.head.data)
            return

        curr = self.head
        prev = None
        count = 0

        while True:
            if count == index:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
            count += 1
            if curr == self.head:
                break

    def display_with_index(self, index):
        if not self.head:
            print("List is empty")
            return

        curr = self.head
        count = 0
        while True:
            if count == index:
                print(f"Data at index {index}: {curr.data}")
                return
            curr = curr.next
            count += 1
            if curr == self.head:
                break
        print("Index out of range")

# ----------------- TEST ---------------------
cll = CircularLinkedList()
for val in [1, 2, 3, 4, 5]:
    cll.append(val)

cll.display()                  # Display entire list
cll.length()                   # Length
cll.search(3)                  # Search
cll.delete_key(3)              # Delete single key
cll.display()
cll.delete_with_index(2)       # Delete by index
cll.display()
cll.display_with_index(1)      # Show data at index
cll.delete_all_keys(1)         # Delete all 1s
cll.display()
