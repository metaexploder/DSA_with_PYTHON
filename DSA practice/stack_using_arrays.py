# ----- my code but it have some issue below this code the correct code by chatgpt
class Stack:
    def __init__(self, length):
        self.stack = [None for _ in range(length)]
        self.length = length
        self.top = -1


    def push(self, data):
        if not s.isFull():
            self.stack[self.top + 1] = data
            self.top += 1
            return True
        return print("Stack Overflow")
        

    def pop(self):
        if s.isEmpty():
            return print("Stack Underflow")
        self.stack.remove(self.stack[self.top])
        self.stack.insert(self.top, None)
        self.top -= 1
        print("Top:", self.stack[self.top])

        
    
    def display(self):
        print(self.stack)
        #print(*(self.stack[i] for i in range(len(self.stack))))

    def peek(self):
        if self.top < 0:
            return print("Stack is empty")
        print(self.stack[self.top])

    def isFull(self):
        if self.top >= self.length - 1:
            return True
    
    def isEmpty(self):
        if self.top == -1:
            return True



s = Stack(5)
# for i in [3, 5, 7, 1]:
#     s.push(i)
s.display()
s.peek()
s.pop()
s.display()

# ------------ chat gpt corrected code ----
# class Stack:
#     def __init__(self, length):
#         self.stack = [None for _ in range(length)]
#         self.length = length
#         self.top = -1

#     def push(self, data):
#         if not self.isFull():
#             self.top += 1
#             self.stack[self.top] = data
#             return True
#         print("Stack Overflow")
#         return False

#     def pop(self):
#         if self.isEmpty():
#             print("Stack Underflow")
#             return None
#         popped = self.stack[self.top]
#         self.stack[self.top] = None
#         self.top -= 1
#         return popped

#     def display(self):
#         print("Stack:", self.stack)

#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Top element:", self.stack[self.top])

#     def isFull(self):
#         return self.top == self.length - 1

#     def isEmpty(self):
#         return self.top == -1
