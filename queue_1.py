class queue:
    def __init__(self):
        self.rear=self.front=-1
        self.size=5
        self.list=[]
    def enqueue(self,data):
        if len(self.list)==5:
            print("full")
            return 0
        self.rear+=1
        self.list.append(data)
        if self.front==-1:
            self.front+=1
    def dqueue(self):
        if len(self.list)==0:
            print("empty")
            return 0
        self.list.pop(0)
        self.front+=1
    def display(self):
        if len(self.list)==0:
            print("empty")
            return 0
        print(self.list)
q=queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(2)
q.enqueue(5)
q.enqueue(6)
q.display()
q.dqueue()
q.dqueue()
q.display()