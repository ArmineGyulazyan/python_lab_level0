class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def is_empty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if not self.is_empty():
            self.queue.pop(0)
        else:
            print("Empty Queue")

    def size_of(self):
        return len(self.queue)

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Empty queue")

    def display(self):
        for i in self.queue:
            print(i, "-->", end='')
        print()


queue = Queue()
queue.enqueue(14)
queue.enqueue(12)
queue.enqueue(13)
queue.enqueue(34)
print(queue.size_of())
print(queue.is_empty())
print(queue.peek())
queue.dequeue()
queue.dequeue()
queue.display()