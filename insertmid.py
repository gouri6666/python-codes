class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insertatend(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=newnode  
    def insertatmid(self,value):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
        else:
            fast=self.head
            slow=self.head
            while fast.next!=None and fast.next.next!=None:
                fast=fast.next.next
                slow=slow.next
            newnode.next=slow.next
            slow.next=newnode
    def printlist(self):
        curr=self.head
        while(curr!=None):
            print(curr.data,"->",end=" ")
            curr=curr.next
        print("null")
l=linkedlist()
l.insertatend(1)
l.insertatend(2)
l.insertatend(3)
l.insertatend(4)
l.insertatend(5)
l.insertatmid(9)
l.insertatmid(8)
l.insertatmid(7)
l.printlist()