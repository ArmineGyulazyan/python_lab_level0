from BSTNode import BSTNode

class DoubleLinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return not self.head

    def append(self, data):
        node = BSTNode(data)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current

    def prepend(self, data):
        node = BSTNode(data)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def delete(self, data):
        current = self.head
        if not self.is_empty():
            while current.next:
                if self.head.data == data:
                    self.head = self.head.next
                    self.head.next.prev = self.head.prev
                    break
                if current.next.data == data:
                    current.next = current.next.next
                    current.next.prev = current.prev
                    break
                current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def insertAfter(self,target_data,data):
        new_node = BSTNode(data)
        current = self.head
        while current:
            if current.data == target_data:
                new_node.next = current.next
                current.next = new_node
                new_node.prev = current
            if new_node.next:
                new_node.next.prev = new_node
                return
            else:
                current = current.next
        # print("Node is not present")

    def insertBefore(self,target_data,data):
        new_node = BSTNode(data)
        if self.head.data == target_data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        current = self.head.next
        while current:
            if current.data == target_data:
                new_node.prev = current.prev
                new_node.next = current
                current.prev.next = new_node
                current.prev = new_node
            # if new_node.prev:
            #     new_node.prev.next = new_node
                return
            current = current.next

        # print("Node is not present")



ob = DoubleLinkedList()
ob.append(15)
ob.append(16)
ob.append(17)
ob.display()
ob.prepend(10)
ob.display()
ob.insertAfter(17,225)
ob.display()
ob.insertBefore(15,100)
ob.display()
ob.delete(16)
ob.display()



