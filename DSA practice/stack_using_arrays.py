# ----- my code but it have some issue below this code the correct code by chatgpt
class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = - 1

    def push(self, data):
        if self.isFull():
            return print("Stack Overflow Error")
        else:
            self.top += 1
            return self.stack.append(data)
        
    def pop(self):
        if self.isEmpty():
            return print("Stack Underflow error")
        else:
            ele = self.stack[self.top]
            self.stack.pop(self.top)
            self.top -= 1
            return print(ele, "is popped")
        
    def display(self):
        return print(self.stack)

    def peek(self):
        if self.top < 0:
            return print("Stack is empty")
        print(self.stack[self.top])

    def isFull(self):
        return self.top >= self.size - 1
    
    def isEmpty(self):
        return self.top == -1
    


s = Stack(5)
for item in [2, 3, 4, 5, 6]:
    s.push(item)

s.display()
s.pop()
s.display()
s.pop()
s.push(9)
s.display()
s.push(0)
s.display()
s.peek()



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
