class node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class trees:
    def __init__(self):
        self.root=None
    def insert(self,value):
        newnode=node(value)
        if self.root is None:
            self.root=newnode
        else:
            curr=self.root
            while True:
                if value<=curr.data:
                    if curr.left is None:
                        curr.left=newnode
                        break
                    else:
                        curr=curr.left
                else:
                    if curr.right is None:
                        curr.right=newnode
                        break
                    else:
                        curr=curr.right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)        
r=trees()
r.insert(5)  
r.insert(4)    
r.insert(3)

inorder(r.root)