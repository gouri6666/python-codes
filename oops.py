class person:
    def __init__(self,x,y,z):
        self.nickname=x
        self.roll=y
        self.height=z
    def run(self):
        print("i can run",self.nickname,self.roll)
gouri=person("chintu",47,5)
vindhu=person("ammu",37,5)
gouri.run()
vindhu.run()          