from Node import Node


class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def is_empty(self):
        return self.size == 0

    def size_of(self):
        return self.size

    def push(self,value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("the stack is empty")
        remove = self.top.value
        self.top = self.top.next
        self.size -= 1
        return remove

    def peek(self):
        return self.top.value

    def display(self):
        current = self.top
        while current:
            print(current.value,"-->",end='')
            current = current.next
        print()

ob = Stack()
ob.push(5)
ob.push(6)
ob.push(7)
ob.display()
print(ob.peek())
ob.pop()
ob.display()


