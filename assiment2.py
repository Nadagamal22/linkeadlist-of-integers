class Node:
    def __init__(self):
        self.data=None
        self.next=None
    def setData(self,data):
        self.data=data
    def getData(self):
        return self.data
    def setNext(self,next):
        self.next=next
    def getMext(self):
        return self.next
    def hasNext(self):
        return self.next!=None

n=Node()
n.setData(5)
print(n.getData())