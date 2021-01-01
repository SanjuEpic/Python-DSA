print('Children Sum Property')
print("\nThis property tells whether the children's sum is equal to the root value")
print('if this property is not followed then the function returns false')
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
root=Node(20)
root.left=Node(8)
root.right=Node(12)
root.left.left=Node(3)
root.left.right=Node(5)
root.right.left=Node(12)
def CSP(root):
    if root==None:
        return 'Yes'
    if root.left==None and root.right==None:
        return 'Yes'
    if root.left==None:
        if root.value==root.right.value:
            return CSP(root.left) and CSP(root.right)
        else:
            return 'No'
    elif root.right==None:
        if root.value==root.left.value:
            return CSP(root.left) and CSP(root.right)
        else:
            return 'No'
    if root.value==(root.left.value+root.right.value):
        return CSP(root.left) and CSP(root.right)
    else:
        return 'No'
print(f' \n Does the above tree follows the Children sum property? \n {CSP(root)}')


## output 
'''Children Sum Property

This property tells whether the children's sum is equal to the root value
if this property is not followed then the function returns false
 
 Does the above tree follows the Children sum property? 
 Yes
 the above tree was :- 
                       20
                       /\
                      8 12
                     /\ /
                    3 5 12
    Try some more examples on binary tree........           
 '''
        
    
