print('Same Tree Problem\n')
print('\n The idea is to traverse the both the trees and check the values of both the trees in that fashion \n if both the traversed values are same then prints true')
print('\n Two types of traversals are level order and depth wise traversal\n We perform inorder traversal here')
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
root=Node(20)
root.left=Node(68)
root.right=Node(132)
root.left.left=Node(575)
root.left.right=Node(365)
root.right.left=Node(21)

root2=Node(20)
root2.left=Node(68)
root2.right=Node(132)
root2.left.left=Node(365)
root2.left.right=Node(575)
root2.right.left=Node(21)

def traverse(root):
    arr=[]
    if root:
        arr+=traverse(root.left)
        arr.append(root.value)
        arr+=traverse(root.right)
    return arr
if traverse(root)==traverse(root2):
    print('  Both the trees are same!!')
else:
    print("  Both the trees are Different structures!:(")

    ''' 
                        20                                    20
                       /  \                                  /  \
                     68   132                              68   132
                     /\    /                               /\   / 
                  575 365 21                           365 575 21
                  Output is false As both the trees are different in structure even though the values are same
    '''
