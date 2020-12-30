# this part contains left-view of Binary tree
class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
right_visited=False
def Trav(root, right_visited):
    arr=[]
    if right_visited!=True:
        arr.append(root.value)
    if root.left!= None:
        arr+=Trav(root.left, False)
    if root.right!=None:
        arr+=Trav(root.right, True)
    return arr
# creation of a binary tree manually
root=Node(12)
root.left=Node(20)
root.left.left=Node(18)
root.left.right=Node(15)
root.left.right.left=Node(68)
root.right=Node(30)
root.right.right=Node(40)
root.right.right.left=Node(50)
root.right.right.right=Node(60)
print(f'Left view of binary tree-> {Trav(root, right_visited)}')
# same can be done for right view of Binary tree by just interchanging the boolean values for left_visited
    
