from Node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def size_of(self):
        return self.size

    def enqueue(self,value):
        node = Node(value)
        if self.is_empty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1

    def dequeue(self):
        if not self.is_empty():
            value = self.front.value
            self.front = self.front.next
            self.size -= 1
        else:
            print("Empty stack")
        return value

    def display(self):
        current = self.front
        while current:
            print(current.value,"-->",end="")
            current = current.next
        print()

    def peek(self):
        return self.front.value

ob = Queue()
ob.enqueue(12)
ob.enqueue(13)
ob.enqueue(14)
ob.enqueue(15)
ob.display()
print(ob.size_of())
print(ob.peek())