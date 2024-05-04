class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insertatbeg(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head 
            self.head=newnode
    def listsearch(self,key):
        curr=self.head
        while curr!=None:
            if curr.data==key:
                print("found")
                break
            curr=curr.next
        else:
            print("not found")          
    def printlist(self):
        curr=self.head
        while(curr!=None):
            print(curr.data,"->",end=" ")
            curr=curr.next
        print("null")
l=linkedlist()
l.insertatbeg(1)
l.insertatbeg(2)
l.insertatbeg(3)
l.insertatbeg(4)
l.insertatbeg(5)
l.printlist()
l.listsearch(8)