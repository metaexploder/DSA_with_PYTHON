class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.top = -1

    def enqueue(self, data):
        if self.isFull():
            print("Queue Overflow Error")
        else:
            self.top += 1
            self.queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow Error")
        else:
            rem = self.queue.pop(0)  # remove from front
            self.top -= 1
            print(f"{rem} is successfully removed")


    def getTOP(self):
        return print(f"Top: {self.queue[self.top]}")
    
    def getbottom(self):
        return print(f"Bottom: {self.queue[0] if self.top > -1 else None}")

    def display(self):
        print(self.queue)

    def isFull(self):
        return len(self.queue) == self.size

    def isEmpty(self):
        return len(self.queue) == 0



q = Queue(5)
for item in [2, 3, 4, 5]:
    q.enqueue(item)

q.display()
q.dequeue()
q.display()
q.enqueue(1)
q.display()
q.enqueue(9)
q.display()
q.dequeue()
q.display()
q.getTOP()
q.getbottom()