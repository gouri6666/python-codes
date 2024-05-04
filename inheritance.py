#SINGLE INHERITANCE
# class parents:
#     def coolness(self):
#         print("parents are cool")
# class child(parents):
#     def cooding(self):
#         print("i know coding")        
# rahul=child()
# rahul.coolness()
# rahul.cooding()                

#MULTILEVEL INHERITANCE
# class parents:
#     def coolness(self):
#         print("parents are cool")
# class child(parents):
#     def cooding(self):
#         print("i know coding") 
# class child2(child):
#     def dance(self):
#         print("i know coding and dancig")               
# rahul=child2()
# rahul.coolness()
# rahul.cooding() 
# rahul.dance()               

#MULTIPLE
# class parents:
#     def coolness(self):
#         print("parents are cool")
# class child:
#     def cooding(self):
#         print("i know coding") 
# class child2(parents,child):
#     def dance(self):
#         print("i know coding and dancig")               
# rahul=child2()
# rahul.coolness()
# rahul.cooding() 
# rahul.dance()               

#HEIRARCHIAL
class parent:
    def coolness(self):
        print("parents are cool")
class child1(parent):
    def cooding(self):
        print("i know coding") 
class child2(parent):
    def dance(self):
        print("i know coding and dancig")               
rahul=child1()
rahul.coolness()
rahul.cooding() 
ammu=child2()
ammu.coolness()
ammu.dance() 

#hybrid
class parent:
    def coolness(self):
        print("parents are cool")
class child1(parent):
    def cooding(self):
        print("i know coding") 
class child2(parent):
    def dance(self):
        print("i know coding and dancig") 
class grandchild(child1,child2):
    def sining(seelf):
        print("i know dancing")                 
rahul=grandchild()
rahul.coolness()
rahul.cooding() 
rahul.dance()
rahul.sining()