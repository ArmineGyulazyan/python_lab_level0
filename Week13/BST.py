class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
       self.root = None

    def isempty(self):
       return not self.root

    def clear(self):
       self.root = None

    def _help_insert(self, node, key, value):
       if node is None:
           return Node(key, value)
       elif node.key < key:
           node.right = self._help_insert(node.right, key, value)
       elif node.key > key:
           node.left = self._help_insert(node.left, key, value)
       else:
           node.value = value
       return node

    def insert(self, key, value):
       self.root = self._help_insert(self.root, key, value)

    def find_max(self):
       current = self.root
       # max_key = self.root.key
       while current.right:
           # if current.right.key > max_key:
           #     max_key = current.right.key
           # else:
           current = current.right
       return current.key

    def find_min(self, node):
       current = node
       while current.left:
           current = current.left
       return current

    def contains(self, key):
       current = self.root
       while current:
           if key == current.key:
               return current.value
           if key < current.key:
               current = current.left
           else:
               current = current.right
       return "Key is not found"

    def search(self, key):
       current = self.root
       while current:
           if key == current.key:
               return True
           if key < current.key:
               current = current.left
           else:
               current = current.right
       return False

    def update(self, key, value):
       current = self.root
       while current:
           if key == current.key:
               current.value = value
               return
           elif key < current.key:
               current = current.left
           else:
               current = current.right
       return "Key not found"

    def size(self):
       size = 0
       if not self.root:
           return size
       current = self.root
       while current.left:
           size += 1
           current = current.left
       current = self.root
       while current.right:
           size += 1
           current = current.right
       return size + 1

    def _help_inorder(self,current_node,res):
       if current_node:
           self._help_inorder(current_node.left,res)
           res.append((current_node.key,current_node.value))
           self._help_inorder(current_node.right,res)

    def inorder(self):
       res = []
       self._help_inorder(self.root,res)
       return res

    def preorder(self):
       res = []
       self._help_preorder(self.root, res)
       return res

    def _help_preorder(self, node, result):
       if node:
           result.append((node.key, node.value))
           self._help_preorder(node.left, result)
           self._help_preorder(node.right, result)

    def postorder(self):
       res = []
       self._help_postorder(self.root, res)
       return res

    def _help_postorder(self, node, result):
       if node:
           self._help_postorder(node.left, result)
           self._help_postorder(node.right, result)
           result.append((node.key, node.value))

    def height(self):
       res = self._help_height(self.root)
       return res

    def _help_height(self, node):
       if not node:
           return -1
       else:
           left = self._help_height(node.left)
           right = self._help_height(node.right)
       return max(left, right) + 1

    def delete(self,node):
        self.root = self._help_delete(self.root,node)

    def _help_delete(self,current_node,key):
        if not current_node:
            return None
        elif key < current_node.key:
            current_node.left = self._help_delete(current_node.left,key)
        elif key > current_node.key:
            current_node.right = self._help_delete(current_node.right,key)
        else:
            if not current_node.left:
                return current_node.right
            elif not current_node.right:
                return current_node.left
            else:
                tmp = self.find_min(current_node.right)
                current_node.key, current_node.value = tmp.key,tmp.value
                current_node.right = self._help_delete(current_node.right,tmp.key)
        return current_node

    def kth_smallest(self, k):
        ls = self.inorder()
        return ls[k - 1]

    def kth_largest(self, k):
        return self.inorder()[-k]

    def copy(self):
        new_tree = BinarySearchTree()
        new_tree.root = self._help_copy(self.root)
        return new_tree

    def _help_copy(self, node):
        if not node:
            return node
        new_tree = Node(node.key, node.value)
        new_tree.left = self._help_copy(node.left)
        new_tree.right = self._help_copy(node.right)
        return new_tree
ob = BinarySearchTree()
ob.insert(22, "m")
ob.insert(12, "e")
ob.insert(30, "eh")
ob.insert(8, "ch")
ob.insert(20, "h")
ob.insert(25, "v")
ob.insert(40, "y")
# ob.insert(33, "o")
print(ob.inorder())
ob.delete(30)
print()
print(ob.inorder())
# print(ob.height())

