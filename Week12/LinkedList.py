class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return not self.head

    def clear(self):
        self.head = None

    def getSize(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next
        return size

    def append(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def prepend(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def deleteNode(self, data):
        current = self.head
        if not self.is_empty():
            while current.next:
                if self.head.data == data:
                    self.head = self.head.next
                    break
                if current.next.data == data:
                    current.next = current.next.next
                    break
                current = current.next

    def printList(self):
        current = self.head
        while current:
            print(current.data, "--> ", end='')
            current = current.next
        print()

    def insertAfter(self,node,data):  # insert data2 after data1, kam mejy grenq __eq__(self,other),vory nodei meja sahmanvum
        if node is None:
            print("The node does not exist")
            return
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node



ob = LinkedList()
ob.append(15)
ob.append(16)
ob.append(17)
print(ob.getSize())
ob.printList()
# ob.prepend(123)
# print(ob.getSize())
# ob.printList()
# ob.deleteNode(16)
# ob.printList()
# print(ob.getSize())
node_insert = ob.head
ob.insertAfter(node_insert.next,44)
ob.printList()


