import random as r
class BTree:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None
  def add_child(self,data):
    if data <= self.data:
      if self.left:
        self.left.add_child(data)
      else:
        self.left= BTree(data)
    else:
      if self.right:  # subtrees
        self.right.add_child(data)
      else:  # traversed till the base node and then inserting
        self.right= BTree(data)

def print_Inorder_traversal(root):
  if root == None:
    return
  print_Inorder_traversal(root.left)
  print(root.data, end='\t')
  print_Inorder_traversal(root.right)

def print_Preorder_traversal(root):
  if root:
    print(root.data,end='\t')
    print_Preorder_traversal(root.left)
    print_Preorder_traversal(root.right)

def print_Postorder_traversal(root):
  if root:
    print_Postorder_traversal(root.left)
    print_Postorder_traversal(root.right)
    print(root.data, end='\t')

# taking random integers within the range of 1-20 for filling a binary tree 

elements=[r.randint(1,20) for i in range(8)]
print(elements)

root=BTree(elements[0])

for i in range(1,len(elements)):
  root.add_child(elements[i])

print('Inorder Traversal of the tree is ->\n')
print_Inorder_traversal(root)
print('\n\nPreorder Traversal of the tree is ->\n')
print_Preorder_traversal(root)
print('\n\nPostorder Traversal of the tree is ->\n')
print_Postorder_traversal(root)
