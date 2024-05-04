class Node:
    def _init_(self,value):
        self.data=value
        self.next=None
class linkedlist:
    def _init_(self):
        self.head=None
    def insertatbeg(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            newnode.next=self.head 
            self.head=newnode
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