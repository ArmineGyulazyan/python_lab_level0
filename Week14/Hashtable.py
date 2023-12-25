class Node:
  def __init__(self,key,value):

    self.key = key
    self.value = value
    self.next = None

class HashTable:

  def __init__(self,size):

    self.size = size
    self.ls = [None for _ in range(self.size)]

  def hash_k(self,key):

    res_hash = hash(key)%self.size
    return res_hash

  def insert(self,key,value):
    node = Node(key,value)
    new_index = self.hash_k(key)

    if not self.ls[new_index]:
      self.ls[new_index] = node
      return
    current = self.ls[new_index]

    while current.next:
      if current.key == key:
        current = node
        return
      current = current.next
    current.next = node

  def get(self,key):
    index = self.hash_k(key)
    current = self.ls[index]
    while current:
      if current.key == key:
        return current.value
      current = current.next
    raise ValueError("Key does not exist")

  def remove(self,key):
    index = self.hash_k(key)
    current = self.ls[index]
    if current.key == key:
      self.ls[index] = current.next
      return
    while current.next:
      if current.next.key == key:
        current.next = current.next.next
        return
      current = current.next

  def display(self):
      for i in range(len(self.ls)):
        if self.ls[i]:
          print(self.ls[i].value)
          current = self.ls[i]
          while current.next:
            current = current.next
            print(current.value)

  def get_keys(self):
    keys = []
    for i in range(len(self.ls)):
      if self.ls[i]:
        keys.append(self.ls[i].key)
        current = self.ls[i]
        while current.next:
          current = current.next
          keys.append(current.key)
    print(keys)

  def get_values(self):
    values = []
    for i in range(len(self.ls)):
      if self.ls[i]:
        values.append(self.ls[i].value)
        current = self.ls[i]
        while current.next:
          current = current.next
          values.append(current.value)
    print(values)

  def get_items(self):
    items = []
    for i in range(len(self.ls)):
      if self.ls[i]:
        items.append((self.ls[i].key,self.ls[i].value))
        current = self.ls[i]
        while current.next:
          current = current.next
          items.append((current.key,current.value))
    print(items)


ob = HashTable(5)
ob.insert("a",1)
ob.insert("b",2)
ob.insert("c",3)
ob.insert("d",4)
ob.insert("e",5)
ob.display()
ob.get("c")
# ob.remove("c")
# ob.display()
ob.get_keys()
ob.get_values()
ob.get_items()