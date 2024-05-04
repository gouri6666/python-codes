class stack:
    def __init__(self):
        self.top=-1
        self.size=5
        self.list=[]
    def push(self,data):
        if len(self.list)==5:
            print("full")
            return 0
        self.top+=1
        self.list.append(data)
    def pop(self):
        if len(self.list)==0:
            print("empty")
            return 0
        self.top-=1
        self.list.pop()
    def peek(self):
        print(self.list)
        if len(self.list)==0:
            print("empty")
            return 0
        elif self.top>5:
            print("out of stack")
        else:
            print(self.list[self.top])
s=stack()
s.push(1)
s.push(2)                     
s.push(3)
s.push(4)
s.push(5)
s.pop()
s.peek()