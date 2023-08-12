# Linked List tutorials
# Regerences : Previous tutorials

class node:
    def __init__(self,data,ref=None):
        self.data = data
        self.ref = ref

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self,data):
        nod = node(data,self.head)
        self.head = nod

    def show(self):
        while self.head:
            d = self.head.data
            self.head = self.head.ref
            print(d)


lnk_list = LinkedList()
for i in range(10):
    lnk_list.add_first(i)

lnk_list.show()