class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    
    def display(self):
        print(i for i in self.stack)

s = Stack()
for i in [3, 5, 7]:
    s.push(i)
s.display()