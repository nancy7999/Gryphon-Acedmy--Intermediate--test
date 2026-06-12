class Father:
    def property(self):
        print("Father has property")

    def business(self):
        print("Father runs a business")


class Son(Father):
    def study(self):
        print("Son is studying")


class Daughter(Father):
    def dance(self):
        print("Daughter is dancing")


class GrandChild(Son, Daughter):
    def gaming(self):
        print("GrandChild is playing games")



g = GrandChild()

g.property()
g.business()
g.study()
g.dance()
g.gaming()